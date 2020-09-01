from selenium import webdriver
import time

PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

text= "Dear Meow, Ishu is sleeping right now! He will reply to your texts when he gets up. BTW this is an auto generated reply from his bot. Thanks!"
# Time provided to scan the QR code of Whatsapp Web
time.sleep(10)

# Click on the Chat
user=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[17]/div/div/div[2]/div[1]/div[1]/span/span')
user.click()

# Type the message on the Chatbox
textbox=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
textbox.send_keys(text)

# Send Message
send=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
send.click()

time.sleep(5)
driver.quit()
