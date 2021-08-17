from os import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from zipfile import ZipFile
from pathlib import Path    


outlink = 'https://binusmaya.binus.ac.id/login/'

def forchrome():
    username_sunib = input('Input Email : ')
    print(' ')
    password_sunib = input('Input Password : ')
    
    browser_chr = webdriver.Chrome()
    browser_chr.get(outlink)
    
    username_browser = browser_chr.find_element_by_xpath('//input[@class="input text"]')
    username_browser.send_keys(username_sunib)
    time.sleep(5)  
    password_browser = browser_chr.find_element_by_xpath('/html/body/div/section[2]/div/form/p[1]/span/input[@type="password"]')
    password_browser.send_keys(password_sunib)
    time.sleep(3)  
    login_button = browser_chr.find_element_by_xpath('//*[@class="button button-primary wide"]')
    login_button.click()
    time.sleep(10)
    
    for i in range(2):
        i = browser_chr.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/button[@class="button button-primary"]').click()
        time.sleep(3)
    
    
    browser_chr.find_element_by_xpath('//*[@class="expand-menu expand-item-menu"]').click()
    browser_chr.find_element_by_xpath('/html/body/div[3]/header/div/section[2]/nav/div/ul[1]/li[1]/div/ul/div/div/div[1]/li[7]/a/span[@class="label"]').click()
    time.sleep(1)
    browser_chr.find_element_by_xpath('/html/body/div[3]/header/div/section[2]/nav/div/ul[1]/li[1]/div/ul[2]/div/div/div[1]/li[8]/a/span[@class="label"]').click()
    time.sleep(1)
    browser_chr.find_element_by_xpath('/html/body/div[3]/header/div/section[2]/nav/div/ul[1]/li[1]/div/ul[3]/div/div/div[1]/li[2]/a/span[@class="label"]').click()


def formozila():
    username_sunib = input('Input Email : ')
    print(' ')
    password_sunib = input('Input Password : ')

    browser_moz = webdriver.Firefox(executable_path=r'/home/artemis/sec_engginier/bot-autologin/geckodriver')
    browser_moz.get(outlink)

    username_browser = browser_moz.find_element_by_xpath('//input[@class="input text"]')
    username_browser.send_keys(username_sunib)
    time.sleep(5)  
    password_browser = browser_moz.find_element_by_xpath('/html/body/div/section[2]/div/form/p[1]/span/input[@type="password"]')
    password_browser.send_keys(password_sunib)
    time.sleep(3)  
    login_button = browser_moz.find_element_by_xpath('//*[@class="button button-primary wide"]')
    login_button.click()
    time.sleep(10)
    
    for i in range(2):
        i = browser_moz.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div[2]/button[@class="button button-primary"]').click()
        time.sleep(3)
    
    
    browser_moz.find_element_by_xpath('//*[@class="expand-menu expand-item-menu"]').click()
    browser_moz.find_element_by_xpath('/html/body/div[3]/header/div/section[2]/nav/div/ul[1]/li[1]/div/ul/div/div/div[1]/li[7]/a/span[@class="label"]').click()
    time.sleep(1)
    browser_moz.find_element_by_xpath('/html/body/div[3]/header/div/section[2]/nav/div/ul[1]/li[1]/div/ul[2]/div/div/div[1]/li[8]/a/span[@class="label"]').click()
    time.sleep(1)
    browser_moz.find_element_by_xpath('/html/body/div[3]/header/div/section[2]/nav/div/ul[1]/li[1]/div/ul[3]/div/div/div[1]/li[2]/a/span[@class="label"]').click()

print('1. Are u user chrome??')
print('2. Are u user firefox??')

choose_statement = input('Input The Number : ')

if choose_statement == "1":
    
    chrome_url = 'https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_win32.zip'
    
    if Path('chromedriver.exe').is_file():
        print('File Exist') 
        forchrome()
    else:
        print('Downloading .... just hold')
        req_chr = requests.get(chrome_url, allow_redirects=True)
        open('chromedriver_win32.zip', 'wb').write(req_chr.content)
        print('Downloading Done....')
        time.sleep(1)
        print('Prepare To Unzip File')
        
        with ZipFile("chromedriver_win32.zip",'r') as zip:
            zip.printdir()
            zip.extractall()
            print('Done..')
        
        forchrome()

else:
    mozila_url = 'https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz'

    if Path('chromedriver.exe').is_file():
        print('File Exist')
        formozila()
    else:
        print('Downloading .... just hold')
        req_moz = requests.get(mozila_url, allow_redirects=True)
        open('geckodriver-v0.29.1-linux64.tar.gz', 'wb').write(req_moz.content)
        print('Downloading Done....')
        time.sleep(1)
        print('Prepare To Unzip File')

        with ZipFile("chromedriver_win32.zip",'r') as zip:
            zip.printdir()
            zip.extractall()
            print('Done..')
        formozila()
