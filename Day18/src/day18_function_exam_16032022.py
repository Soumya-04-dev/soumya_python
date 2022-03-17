import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path='/home/sohil/soumya_python/soumya_python/Day18/src/Browser/chromedriver')


def navigate_url():
    print(f'open chrome browser')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    print(f'maximize the chrome browser window')
    driver.maximize_window()
    print(f'navigate to the url')


#   driver.get("https://www.google.com/")


navigate_url()
