#!/bin/bash
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
cd $SCRIPTPATH
source venv/bin/activate
printf "\n\n\n\n\nLaunching DIY Transparency application server. Please leave this window open throughout your use of the app.\n\n\n\n\n"
python app.py