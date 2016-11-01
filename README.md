#DIY Transparency
DIY Transparency is an application that makes it simpler to define and create transparency reports for your organization.

DIY Transparency is a Python application that runs a webserver that serves a web interface. Point your web browser to http://localhost:5000 to use the app.

See Appendix II of [A Guide to Transparency Reporting for Canadian Businesses Using the DIY Transparency Report Tool for usage instructions](https://www.telecomtransparency.org/wp-content/uploads/2016/06/Transparency-Reporting-Tool-Documentation-1.0.pdf).

## Installing and opening the app
We provide some useful scripts for Windows and Mac users to make it easier to install and launch the applicaiton.

### Windows
Make sure you have Python 2 installed on your machine. https://www.python.org/downloads

Next, double click on `windows-install-pip.bat` to install pip (or install it following the official guide: https://pip.pypa.io/en/stable/installing/)

Next, double click `windows-install-requirements.bat` to install the required software libraries.

Finally, double click `windows-diy-transparency-run.bat` to run the app. Make sure you keep the command prompt window open while you use the app.

### Mac
Double click on `DIY Transparency.app` to launch the app. Before launching the app, it will install the required software libraries if they don't exist. Make sure you keep the terminal window open while you use the app.

**NOTE: You'll need to give `DIY Transparency.app` permission to run on your computer. If you don't want to do that you can always just run the `mac_os.sh` bash script directly.**

### Linux
Make sure you have Python 2 and pip installed.

In the terminal, in the project folder, run:

	pip install -r requirements.txt
	python app.py

