from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string


#type number of account you want to create
number = int(input("Put number of account you want to create"))

browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')

for no_of_account in range(number):
    #generating full name
    boyNames = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan"
             "Babatunmise", "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn"]
    girlNames = ["Alice", "Hana", "Clare", "Janet", "Daisy"]
    fnameStr = ''.join(random.choice(boyNames) + ' '  + random.choice(girlNames))
    print(fnameStr)

    #generating a username of 7 length
    size = 7
    chars  = string.ascii_lowercase + random.choice(['.', '_'])
    usernameStr = ''.join(random.choice(chars) for _ in range(size))
    print(usernameStr)

    #password
    passwordStr = "intime@lpu"
    print(passwordStr)

    #generating email id
    emailStr = ''.join(usernameStr + "@gmail.com")
    print(emailStr)

    #writing details in text file
    file1 = open("account_details", "a")
    row = [fnameStr,' ', usernameStr,' ', passwordStr, ' ', emailStr, '\n']
    file1.writelines(row)
    file1.close()
    
    time.sleep(10)
        
    #to open instagram link in the browser
    browser.get(('https://www.instagram.com/accounts/emailsignup/?hl=en'))

    # geting all the input fields from the instagram page using css selector
    email = browser.find_elements_by_css_selector('form input')[0]
    fname= browser.find_elements_by_css_selector('form input')[1]
    username=browser.find_elements_by_css_selector('form input')[2]
    password=browser.find_elements_by_css_selector('form input')[3]

    #submiting the value in the instagram input field
    email.send_keys(emailStr)
    time.sleep(5)
    fname.send_keys(fnameStr)
    time.sleep(5)
    username.send_keys(usernameStr)
    time.sleep(5)
    password.send_keys(passwordStr)

    #click on the submit button
    browser.find_elements_by_css_selector('form input')[3].submit()

    time.sleep(10)  #to click on not now on notification tab
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
    time.sleep(5)   #to click on profile
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span').click()
    time.sleep(5)   #to click on settings
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span').click()
    time.sleep(5)   #to click on log out
    browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/button[6]').click()

# end of for loop
