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







        


        







# ageElem = appSoup.select('#roundup_infobox_age .data')[0]
# overallRatingsElem = appSoup.select('#roundup_infobox_rating .data')[0]
# globalRankElem = appSoup.select('#roundup_infobox_ranking .data')[0]
# descriptionElem = appSoup.select('div[itemprop="description')[0]
# screenshotsElem = appSoup.select('img[class="primary_screenshots"]')
# urls_Elems = []
# for i in screenshotsElem:
#     src = i.get('src')
#     urls_Elems.append(src)
    





