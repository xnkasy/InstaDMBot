from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep
#Select the driver, In our case we will use Chrome.
chromedriver_path = '/usr/local/bin/chromedriver' # Change this to your own chromedriver path!
user=str(raw_input('Username: '))
pswd=str(raw_input('Password: '))
receiver=str(raw_input('To who? :'))
message=str(raw_input('What is the message?: '))
num=int(raw_input('How many times? '))
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
webdriver.get('https://www.instagram.com/direct/inbox/')
username = WebDriverWait(webdriver, 15).until(
    lambda d: d.find_element_by_name('username')
)
username.send_keys(user)
password = webdriver.find_element_by_name('password')
password.send_keys(pswd)

#instead of searching for the Button (Log In) you can simply press enter when you already selected the password or the username input element.
submit = webdriver.find_element_by_tag_name('form')
submit.submit()
notNowButton = WebDriverWait(webdriver, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
)
notNowButton .click()
sleep(3) # need to remove this hard code
el2 = WebDriverWait(webdriver, 15).until(
    lambda d: d.find_elements_by_xpath("//*[contains(text(), 'xnkasy')]")
)

for x in el2:
    if(x.text==receiver):
        x.click()
for i in range(num):
    text = webdriver.find_element_by_xpath("//textarea[@placeholder='Message...']")
    text.clear()
    text.send_keys(message)
    el2=webdriver.find_elements_by_xpath("//*[contains(text(), 'Send')]")
    el2[0].click()
