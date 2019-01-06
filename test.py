from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""proxy =  "192.18.17.153"

class AccountCreator():
    def __init__(self, use_custom_proxy):
        self.sockets = []
        self.use_custom_proxy = use_custom_proxy
        self.url = 'https://www.instagram.com/'
        self.__collect_sockets()

def createaccount(proxy):
        chrome_options = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
        chrome_options.add_argument('--proxy-server=%s' % proxy)

        driver = webdriver.Chrome(chrome_options=chrome_options)
        #browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get('https://www.instagram.com/')"""

from selenium import webdriver
import time

#PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT
usernameStr = 'nisha14029315678kumari'
passwordStr = 'intime@lpu'
emailStr = 'nisha14029315678kumari@gmail.com'
fnameStr = 'Nisha Kumari'

chrome_options = Options()
chrome_options.add_argument("192.168.0.34:8080")
browser = webdriver.Chrome('C:/Users/Nishant/Downloads/chromedriver_win32/chromedriver.exe')

#chrome = webdriver.Chrome(options=chrome_options)
browser.get('https://www.instagram.com/accounts/emailsignup/?hl=en')



email = browser.find_elements_by_css_selector('form input')[0]
fname= browser.find_elements_by_css_selector('form input')[1]
username=browser.find_elements_by_css_selector('form input')[2]
password=browser.find_elements_by_css_selector('form input')[3]

#username = browser.find_element_by_id('/*[.*]/*')
email.send_keys(emailStr)
time.sleep(5)
fname.send_keys(fnameStr)
time.sleep(5)
username.send_keys(usernameStr)
time.sleep(5)
password.send_keys(passwordStr)

browser.find_elements_by_css_selector('form input')[3].submit()
