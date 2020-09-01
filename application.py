from selenium import webdriver
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
# unreadMsgs = browser.find_elements_by_xpath(".//span[span[@class='unread-count icon-meta'] and not(span[@class='icon icon-meta icon-muted'])]")
