import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def navigate_url():
    print(f'open chrome browser')
    driver = webdriver.Chrome('/home/sohil/soumya_python/soumya_python/Day18/src/Browser/chromedriver')
    time.sleep(2)
    print(f'maximize the chrome browser window')
    driver.maximize_window()
    time.sleep(2)
    print(f'navigate to the url')
    driver.get("https://www.google.com/")
    time.sleep(2)
    print(f'Enter the text')
    driver.find_element(by=By.NAME, value="q").send_keys('facebook')
    time.sleep(2)
    print(f'Click on Enter button')
    driver.find_element(by=By.NAME, value="btnK").send_keys(Keys.ENTER)
    time.sleep(2)
    print(f'Close the browser')
    driver.close()



navigate_url()
