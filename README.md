# Run Automated Browser Test

## Prerequisite

1. ) [Python3.6.8](https://www.python.org/downloads/release/python-368/)

**Note** When installing Python 3.6.8 in windows please ensure that you **ADD PATH**

2. ) [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Your Chrome Driver extract to **C://** in a folder called **webdriver** and to the driver to **ADD PATH**

## Set Up and Run 

After you have installed Python and set up you chrome driver user *cmd* to *cd* in project 

1. ) Create Virtual Environment
```bash
python -m venv dev
```

2. ) Switch to virtual environment
```bash
dev\Scripts\activate.bat #win

or 

dev\bin\activate #unix or linux
```

3.) install all requirements 

```bash
pip install -r requirements.txt
```

4.) Run 

```bash
python dashboard_test/test_ciibo_demo_web_app.py
```

Documented by **TeamAvengers**