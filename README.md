# Automated Whatsapp

Usually, my close friends WhatsApp me late at night regarding some work thinking that I'm awake and will reply before morning. 
Thus, I made this WhatsApp bot using selenium in Python which automatically responds to your close friend's text (if they send one) that you're sleeping and thus won't be able to reply before morning!
Also, when you wake up, you'll know who texted you!

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

![reply](https://user-images.githubusercontent.com/45245975/91994219-fd8a7700-ed53-11ea-9666-c8c348adbb91.PNG)
After every 5 minutes, the bot checks for every person you've specified in the closefriends list, that if there is any unread text from their side or not. 
If you've received one, then it replies with the message specified.
Else does nothing.
