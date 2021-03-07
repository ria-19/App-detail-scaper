#!/usr/bin/env python3
# scrape_app.py - Takes app name and provides age, overall ranking, global rank ,
# description and screenshots of that app.


import requests, webbrowser, bs4

from app_class import App

# TODO: takes app name as input dynamically from user
# app_name = input("App to be searched: ")

# Searches for app asked by user and download the page.
res = requests.get('https://www.apptrace.com/app/363590051')
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







        


        












