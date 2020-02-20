from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config import Config

def chooser():
    if Config.get("browser") == 'firefox':
        return firefox_options()
    else:
        return chrome_options()

def firefox_options():
    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = webdriver.Firefox(executable_path=Config.get("firefox_path"), options=opts)
    return browser

def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    browser = webdriver.Chrome(executable_path=Config.get("chrome_path"), chrome_options=options)
    return browser
