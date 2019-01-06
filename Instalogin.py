from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import string

f=open("account_details","r" ) #reading file in read mode
line=f.readline().strip()  #striping the line values from the file 
count=0
browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
while line!="":
    count=count+1 # conuting number of account
    first,last,user,pswd,email=line.split(" ")  #storing the username, firstname, pswd and emailid into variables from lines of file
    #print(first,last,user,pswd,email)
    browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
    # wait for transition then continue to fill items
    username = browser.find_elements_by_css_selector('form input')[0]
    username.send_keys(user)
    time.sleep(5)
    password =browser.find_elements_by_css_selector('form input')[1]
    password.send_keys(pswd)
    time.sleep(5)
    #logging in with submitting the data
    browser.find_elements_by_css_selector('form input')[1].submit()
    time.sleep(5)
    #click on not now for notification tab
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
    time.sleep(5)
    #input user id link whom you want to follow
    browser.get('https://www.instagram.com/tarique_31/')
    time.sleep(5)
    #clicking on the follow button
    follow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
    ActionChains(browser).move_to_element(follow).click().perform()
    time.sleep(7)
    #steps for logout
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span').click()
    time.sleep(5)   #to click on settings
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span').click()
    time.sleep(5)   #to click on log out
    browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/button[6]').click()
    #reading the nextline data
    line=f.readline().strip()
    time.sleep(5)


