# Automated Whatsapp

After I sleep, many a times some of my close friends whatsapp me regarding some work expecting that I'm awake and will reply soon(which ain't possible for sure). Thus, I made this whatsapp bot in PYTHON 3.x which tells your closed friends that you're sleeping and will reply as soon as you get up!

## Requirements
Python 3.x with selenium installed

**Install Python from here:** https://www.python.org/downloads/

**Install Selenium Using command:** pip install selenium

## How to use the bot?

1. Run the code.
2. The code will automatically open Whatsapp Web in Chrome where you're supposed to scan the QR code.
![whatsapp_web](https://user-images.githubusercontent.com/45245975/91994399-30346f80-ed54-11ea-91a2-098d851ac10d.PNG)
3. Sleep Well! :)

## Working of the bot

After every 5 minutes, the bot checks for every person you've specified in the closefriends list, that if there is any unread text from their side or not. 
If you've received one, then it replies with the message specified.
![reply](https://user-images.githubusercontent.com/45245975/91994219-fd8a7700-ed53-11ea-9666-c8c348adbb91.PNG)
Else does nothing.
