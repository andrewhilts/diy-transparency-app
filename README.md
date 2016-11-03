#DIY Transparency Report
DIY Transparency Report is an application that makes it simpler to define and create transparency reports for your organization.

DIY Transparency Report is a Python application that runs a webserver that serves a web interface. Point your web browser to http://localhost:5000 to use the app.

See Appendix II of [A Guide to Transparency Reporting for Canadian Businesses Using the DIY Transparency Report Tool for usage instructions](https://www.telecomtransparency.org/wp-content/uploads/2016/06/Transparency-Reporting-Tool-Documentation-1.0.pdf).

## Installing and opening the app
We provide some useful scripts for Windows and Mac users to make it easier to install and launch the application.

### Windows
Make sure you have Python 2.7.x installed on your machine (The below scripts assume Python is installed to C:\Python27). https://www.python.org/downloads

Next, if you don't have pip installed, install it following the official guide: https://pip.pypa.io/en/stable/installing/

Next, double click `windows-install.bat` to install the required software libraries.

Finally, double click `windows-diy-transparency-run.bat` to run the app. Make sure you keep the command prompt window open while you use the app.

### Mac
Open up the project folder in finder.

Right click on `install.sh`, hover over to "Open With", select "other", choose "Terminal". 

Once that's done, exit Terminal.

Next, to run the app, right click on `diy-transparency-run.sh`, hover over to "Open With", select "other", choose "Terminal". Make sure you keep the Terminal window open while you use the app.

### Linux
Make sure you have Python 2.7.x, pip, and virtualenv (apt-get install virtualenv) installed.

In the terminal, in the project folder, run

	bash install.sh

Once installation is, to launch the app server you can run:

	bash diy-transparency-run.sh

