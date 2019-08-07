import time
import selenium
from selenium import webdriver


def chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    return chrome_options

mylogin = '###@##.##'
mypasswd = '#####'

def log_in():
    # Set driver
    driver = webdriver.Chrome(chrome_options=chrome_options())
    driver.get('https://pl.forgeofempires.com/')
    # Log In
    driver.find_element_by_id('login_userid').send_keys(mylogin)
    driver.find_element_by_id('login_password').send_keys(mypasswd)
    driver.find_element_by_id('login_Login').submit()
    time.sleep(3)
    driver.find_element_by_class_name('play_button').click()
    time.sleep(3)
    driver.find_element_by_link_text('Brisgard').click()
    # Wait for loading page:
    time.sleep(30)
    return driver
