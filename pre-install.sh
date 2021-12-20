set -x
sudo apt-get update -y
sudo apt-get install -y ansible git
sudo ansible-galaxy collection install community.docker
ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "zadon@yandex.ru"
cat ~/.ssh/id_rsa.pub
git config --global user.name "Zadonsky Alexander"
git config --global user.email "zadon@yandex.ru"
echo 'git clone git@github.com:zadon/linuxDevOpsTools.git'
