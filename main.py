from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import shutil

USERNAME = your_user_name
PASSWORD = your_password
def get_class_list():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://my.wgu.edu")
    time.sleep(1)
    # #Username
    elem = driver.find_element(By.XPATH, '//*[@id="login-username"]')
    elem.send_keys(USERNAME)
    # #Password
    elem = driver.find_element(By.ID, "login-password")
    elem.send_keys(PASSWORD, Keys.ENTER)
    #Degree Plan
    time.sleep(1)
    elem = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-header/wgu-header/header/div/div/div[1]/wgu-menu/div/ul/li[3]/span/a')
    elem.click()
    time.sleep(5)
    elems = driver.find_elements(By.CSS_SELECTOR, "a.ng-star-inserted")

    #Saving the list as a text file for formatting later
    with open("classList.txt", "w") as file:
        for each in elems:
            file.write(each.text + "\n")
    # Uncomment to save a backup
    #shutil.copyfile("classList.txt", "backupList.txt")
#get_class_list()
with open("classList.txt", "r") as file:
    rawlist = file.readlines()
#formatting the class list
rawlist = [each.strip("\n") for each in rawlist]
rawlist = [each for each in rawlist if each][4:]


with open ("classList.txt", "w") as file:
    for each in rawlist:
        file.write(each + "\n")