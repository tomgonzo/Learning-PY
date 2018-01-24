#Chapter 18 ChapterNotes - Package Managers!

### Package Manager! ###
#A Package Manager is a program that installs and manages other programs.
#For example, web developers often use a web framework: a program that
#helps to build a website. 

#We will learn the package manager pip

### Packages! ###
#A package is software "packaged" for distribution - it includes the file
#that makes up the actual program, as well as metadata like the software
#name, version number, and dependencies.

#Package Managers download and install packages as programs on the computer.
#It also handles downloading any dependencies it needs.

### PIP!! ###

#pip is a package manager for python.
#Once downloaded, a package can be imported as a module in a Python program.

#New packages can be installed using the syntax:

pip install [packagename]

#There is a list of all available python packages at: pypi.python.org/pypi

#There are two ways to specify the package you want to download:
#the package name, or the package name followed by two equal signs and version

#Using the package name downloads the most recent version of the package.

#To install flask, a package manager for creating websites on Ubuntu and Unix,

sudo pip install Flask==0.11.1

#This installs Flask in the computer's site-packages folder.

#Now you can import the Flask module in a program. Example:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, World!"

app.run(port='8000')