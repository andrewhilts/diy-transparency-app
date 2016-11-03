#!/bin/bash
SCRIPTPATH=${BASH_SOURCE[${#BASH_SOURCE[@]} - 1]}
DIRECTORY=$(dirname "${SCRIPTPATH}")
cd "${DIRECTORY}"
if ! type "virtualenv" > /dev/null; then
	pip install --user virtualenv
	if [ "$(uname)" == "Darwin" ]; then
		echo 'export PATH=/Users/$USER/Library/Python/2.7/bin:$PATH' >> ~/.bash_profile
		source ~/.bash_profile
	fi
fi
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
python venv/bin/pip install -r requirements.txt
printf "\n\n\n\n\nInstallation complete! Run diy-transparency-run.sh to launch the app.\n\n\n\n\n"
exit