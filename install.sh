#!/bin/bash
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
ln -s .DIY\ Transparency.app DIY\ Transparency.app