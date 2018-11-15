from webbrowser import Chrome

from selenium import webdriver

import json

with open('gal.json', 'r') as f:
    obj = json.load(f)
    print(obj['SUT']['prod'])


# driver = webdriver.Chrome()
# driver.get("https://www.kainos.pl/blog/first-test-python-webdriver-pycharm/")
