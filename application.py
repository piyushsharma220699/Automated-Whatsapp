from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

# Texts which you want to send
text= "Dear "
text2=", He is sleeping right now! He will reply to your texts when he gets up. BTW this is an auto generated reply from his bot. Thanks!"

# Time provided to scan the QR code of Whatsapp Web
time.sleep(10)

# List of names to which you want to send the message
namelist = ["Meow","Mom"]


for name in namelist:
    # Click on the search-bar 
    getsearchbox = driver.find_element_by_xpath("//div[@class ='_3FRCZ copyable-text selectable-text']")
    getsearchbox.click()
    time.sleep(2)

    # Type the name of contact
    getsearchbox.send_keys("Mom")
    time.sleep(3)

    # Click on the Chat
    user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # Type the message on the Chatbox
    textbox=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textbox.send_keys(text)
    textbox.send_keys(name)
    textbox.send_keys(text2)

    # Send Message
    send=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    send.click()

    time.sleep(5)

driver.quit()
