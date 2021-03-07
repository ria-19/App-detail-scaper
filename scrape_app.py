#!/usr/bin/env python3
# scrape_app.py - Takes app name and provides age, overall ranking, global rank ,
# description and screenshots of that app.

# import modules
import requests, webbrowser, bs4, sys

<<<<<<< HEAD
# import App class
=======
import requests, webbrowser, bs4, sys

>>>>>>> 6ccd42a2dce44bdd8c35fcb727839fc690b5c145
from app_class import App

#Takes app name as argument dynamically from user
app_name = ' '.join(sys.argv[1: ])


#Requests for app page
res = requests.get("https://www.apptrace.com/app?query=" + app_name)
try:
    res.raise_for_status()
except Exception as exc:
    print("ERROR!")

#Beautiful soup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Scrapes out the redirected link
linkElem = soup.select_one('div .link a').get('href')

# Searches for app asked by user and download the page.
res = requests.get('https://www.apptrace.com' + linkElem)
try:
    res.raise_for_status()
except Exception as exc:
    print("ERROR!")

# Converts into Beautiful object
content = bs4.BeautifulSoup(res.text, 'html.parser')


# Scrapes information about required parameters.
app = App(content)

#Prints to the console
print(app.__dict__)







        


        












