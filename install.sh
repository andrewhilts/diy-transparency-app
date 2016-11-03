#!/bin/bash
if ! type "virtualenv" > /dev/null; then
	curl -L -o virtualenv.py https://raw.github.com/pypa/virtualenv/master/virtualenv.py
	python virtualenv.py -p /usr/bin/python2.7 venv
else
	virtualenv -p /usr/bin/python2.7 venv
fi
source venv/bin/activate
pip install -r requirements.txt
exit