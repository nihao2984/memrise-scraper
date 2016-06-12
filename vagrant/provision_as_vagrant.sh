#!/bin/bash

# add comments to end of .profile and .bashrc
PROFILE="/home/vagrant/.profile"
BASHRC="/home/vagrant/.bashrc"
COMMENT="\n#\n# Vagrant provision script\n#\n\n"
grep -q -F "Vagrant provision script" $PROFILE || printf "$COMMENT" >> $PROFILE
grep -q -F "Vagrant provision script" $BASHRC || printf "$COMMENT" >> $BASHRC

# .profile
CMD="export PYTHONDONTWRITEBYTECODE='1'"
grep -q -F "$CMD" $PROFILE || echo "$CMD" >> $PROFILE

# .bashrc
sed -i 's/#force_color_prompt/force_color_prompt/' .bashrc
CMD="source /usr/local/bin/virtualenvwrapper.sh"
$CMD
grep -q -F "$CMD" $BASHRC || echo "$CMD" >> $BASHRC

# Py2 virtualenv
cd /vagrant
if [ ! -d /home/vagrant/.virtualenvs/py2 ]; then
    echo "Python 2 virtualenv does not exist, creating ..."
    mkvirtualenv py2
    pip install -q pip==8.1.1
    pip install -q pip-tools
    setvirtualenvproject
else
    echo "Python 2 virtualenv already exists, updating ..."
    workon py2
fi
pip-sync
deactivate
cd ~
echo "Done."

# Py3 virtualenv
cd /vagrant
if [ ! -d /home/vagrant/.virtualenvs/py3 ]; then
    echo "Python 3 virtualenv does not exist, creating ..."
    mkvirtualenv --python=$(which python3) py3
    pip install -q pip==8.1.1
    pip install -q pip-tools
    setvirtualenvproject
else
    echo "Python 3 virtualenv already exists, updating ..."
    workon py3
fi
pip-sync
deactivate
cd ~
echo "Done."
