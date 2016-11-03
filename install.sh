#!/bin/bash
if ! type "virtualenv" > /dev/null; then
	pip install --user virtualenv
	if [ "$(uname)" == "Darwin" ]; then
		echo 'export PATH=/Users/$USER/Library/Python/2.7/bin:$PATH' >> ~/.bash_profile
		source ~/.bash_profile
	fi
fi
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
exit