#!/bin/bash

date >> /etc/vagrant_provisioned_at

# Essentials
apt-get update -qq
apt-get install -y vim git htop

# Python
apt-get install -y python-pip python-dev python3-dev libxml2-dev libxslt1-dev libffi-dev libssl-dev
pip install -q virtualenv virtualenvwrapper
