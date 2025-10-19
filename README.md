# Robot Driver
A Python program that can automatically perform a task on a website.

## Getting Started
### Virtual Environment 
Create a virtual environment to install the following packages.
If you do not have a virtual environment for python3 installed and are on a Debian/Ubuntu based system:
```
apt install python3.13-venv
```

Go into the directory of the file you would like to create your virtual environment in. This should be '../backend'.
```
cd backend/
```

Run the following to make the needed files:
```
python -m venv .
```

#### On Linux Systems
Activate your virtual environment:
```
source bin/activate
```

#### On Windows Systems
Change to the Scripts directory:
```
cd Scripts
```

Activate your virtual environment:
```
.\activate
```


### Pip
If you do not have pip installed:
```
sudo apt install python3-pip
```

To install Playwrite:
```
pip install --upgrade pip
python -m playwright install
```

Alternatively, if you are running into upgrade issues:
```
python.exe -m pip install --upgrade pip
```

## Credits
The details for the installation were compiled from the following sources. Thank you.
* https://ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/
* https://playwright.dev/python/docs/library
* https://thunderbit.com/blog/playwright-python-tutorial

