![DIY Transparency Report Logo][logo]

#DIY Transparency Report

DIY Transparency Report is an application that makes it simpler to define and create transparency reports for your organization.

DIY Transparency Report is a Python application that runs a webserver that serves a web interface. Point your web browser to http://localhost:5000 to use the app.

See Appendix II of [A Guide to Transparency Reporting for Canadian Businesses Using the DIY Transparency Report Tool for usage instructions](https://www.telecomtransparency.org/wp-content/uploads/2016/06/Transparency-Reporting-Tool-Documentation-1.0.pdf).

## Installing and opening the app
We provide some useful scripts to make it easier to install and launch the application.

Step one: press "Clone or download", follow the instructions, then once you have a copy of the project on your computer, open up the project folder.

### Windows
Make sure you have Python 2.7.x installed on your machine (The below scripts assume Python is installed to C:\Python27). https://www.python.org/downloads

Next, if you don't have pip installed, install it following the official guide: https://pip.pypa.io/en/stable/installing/ (It should install along with Python)

Next, double click `windows-install.bat` to install the required software libraries.

Finally, double click `windows-diy-transparency-run.bat` to run the app. Make sure you keep the command prompt window open while you use the app.

### Mac
Open up Terminal. type `cd` followed by a space. Drag the project folder into Terminal. Hit return.

To install the app:

1.  type `./install.sh` into your Terminal window and hit Enter.

Next, to run the app:

1.  Open up the "Terminal" application. Make sure you are in the project directory.
1.  type `./diy-transparency-run.sh` into your Terminal window and hit Enter.

Make sure you keep the Terminal window open while you use the app.

You can also follow the Linux instructions if you're comfortable with the command line.

### Linux
Make sure you have Python 2.7.x, pip, and virtualenv (apt-get install --user virtualenv) installed.

In the terminal, in the project folder, run

	./install.sh

Once installation is complete, to launch the app server you can run:

	./diy-transparency-run.sh

Make sure you keep the Terminal window open while you use the app.

[logo]: https://raw.githubusercontent.com/andrewhilts/diy-transparency-app/master/static/diy-transparency-logo.png
