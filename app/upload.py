#!/usr/bin/python3
import os
from dotenv import load_dotenv, find_dotenv

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from werkzeug.utils import secure_filename

load_dotenv(find_dotenv())

upload = Blueprint('upload', __name__)
UPLOAD_FOLDER = os.environ.get('DIR')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect('./files')
    return render_template('upload.html')
