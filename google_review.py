from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

f=open("gmail_details","r" ) #reading file in read mode
line=f.readline().strip()  #striping the line values from the file 
count=0
while line!="":
    count=count+1 # conuting number of account
    email,password=line.split(" ")  #storing the username, firstname, pswd and emailid into variables from lines of file
    #print(first,last,user,pswd,email)
    #browser.get(('https://www.google.com/search?source=hp&ei=fMExXPGFBYj6vgSAt7LoBA&q=rush+hrs&btnK=Google+Search&oq=rush+hrs&gs_l=psy-ab.3..0j0i10l2j0l2j0i10l2j0.1966.9794..10400...14.0..0.194.2700.0j20......0....1..gws-wiz.....6..35i39j0i131j0i67j0i22i10i30j0i22i30.skfQQ5HSGWY#btnK=Google%20Search&lrd=0x3bc2bed74650467d:0x5d40200bdac67756,1,,,'))
    browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
    browser.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(5)
    email_id = browser.find_element_by_id('identifierId')
    email_id.send_keys(email)
    browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(5)
    pswd = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pswd.send_keys(password)
    browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
    time.sleep(5)
    #browser.findElement(By.linkText("urlLink")).sendKeys(selectLinkOpeninNewTab);
    browser.get(('https://www.google.com/search?source=hp&ei=fMExXPGFBYj6vgSAt7LoBA&q=rush+hrs&btnK=Google+Search&oq=rush+hrs&gs_l=psy-ab.3..0j0i10l2j0l2j0i10l2j0.1966.9794..10400...14.0..0.194.2700.0j20......0....1..gws-wiz.....6..35i39j0i131j0i67j0i22i10i30j0i22i30.skfQQ5HSGWY#btnK=Google%20Search&lrd=0x3bc2bed74650467d:0x5d40200bdac67756,1,,,'))
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="wrl"]').click()
    time.sleep(5)
    #reading the nextline data
    line=f.readline().strip()
    time.sleep(5)
    browser.close()



"""i=0
emailStr = 'nishantpal123@gmail.com'
pswdStr = 'proxy123@proxy'
browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
#browser.get(('https://www.google.com/search?source=hp&ei=fMExXPGFBYj6vgSAt7LoBA&q=rush+hrs&btnK=Google+Search&oq=rush+hrs&gs_l=psy-ab.3..0j0i10l2j0l2j0i10l2j0.1966.9794..10400...14.0..0.194.2700.0j20......0....1..gws-wiz.....6..35i39j0i131j0i67j0i22i10i30j0i22i30.skfQQ5HSGWY#btnK=Google%20Search&lrd=0x3bc2bed74650467d:0x5d40200bdac67756,1,,,'))
browser.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(5)
email_id = browser.find_element_by_id('identifierId')
email_id.send_keys(emailStr)
browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(5)
pswd = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pswd.send_keys(pswdStr)
browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(5)
#browser.findElement(By.linkText("urlLink")).sendKeys(selectLinkOpeninNewTab);
browser.get(('https://www.google.com/search?source=hp&ei=fMExXPGFBYj6vgSAt7LoBA&q=rush+hrs&btnK=Google+Search&oq=rush+hrs&gs_l=psy-ab.3..0j0i10l2j0l2j0i10l2j0.1966.9794..10400...14.0..0.194.2700.0j20......0....1..gws-wiz.....6..35i39j0i131j0i67j0i22i10i30j0i22i30.skfQQ5HSGWY#btnK=Google%20Search&lrd=0x3bc2bed74650467d:0x5d40200bdac67756,1,,,'))
time.sleep(10)
browser.find_element_by_xpath('//*[@id="wrl"]').click()
time.sleep(5)
#for element in browser.find_elements_by_class_name('tile rating-tile'):
    #print (element.text)
element = browser.find_elements_by_class_name('rating')
print("a")
print(element)
i = i + 1;
print(i)
print("a")
#for element in browser.find_elements_by_class_name('rating-star'):
#    print (element.text)
#browser.find_elements_by_class_name('rating')[4].click()
#time.sleep(2)"""

"""
#browser.find_elements_by_css_selector('form input')[1].click()
#time.sleep(2)
#browser.find_element_by_xpath('//*span[@aria-label="Four stars"]').click();
comments = 'good'
cmnts = browser.find_elements_by_css_selector('form input')[2]
cmnts.send_keys(comments)
browser.close()"""

