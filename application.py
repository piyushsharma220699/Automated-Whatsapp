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

while(1):
    for name in namelist:
        # Click on the search-bar 
        getsearchbox = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        getsearchbox.click()
        time.sleep(2)

        # Type the name of contact
        getsearchbox.send_keys(name)
        time.sleep(3)

        # Check if there is any unread message
        unreadMsgs=False

        getlist=driver.find_elements_by_xpath("//span[@class ='_31gEB']")
        if(len(getlist)):
            unreadMsgs=True

        
        # If there is no unread message, then click on back in the search bar
        if not unreadMsgs:
            cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button")
            cutit.click()
        
        # If an unread message exists, reply to the contact
        else:
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
    
    # The code will run again after 300 seconds (5 Minutes)
    time.sleep(300)

driver.quit()
