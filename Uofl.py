#Program will not work if there is no location/time

#for the project make a function that will determine if the location is valid and then it will add everything to a string
#it will then maybe add everything to a list and it will then be printed out for the user
#https://stackoverflow.com/questions/72446424/how-can-i-solve-this-nonetype-web-scraping-attribute-error-in-the-following-code

from bs4 import BeautifulSoup
import requests
import re
import pywhatkit

#Stuff to make web scrapper work
url = "https://events.louisville.edu/calendar"
results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")


food = ("free", "lunch", "grill", "food", "coffee", "pizza", "ice cream" , "ice-cream", "red barn", "dinner")
'''Enter your number'''
num = ""
msg = ""








for i in doc.find_all("div", class_="item event_item vevent"):
    for j in food:
        try:
            description = i.find("h4", class_="description").string.lower()
            desc = description.find(j)
            if(description.find(j) > 0):
                try:
                    msg+="Title:"
                    msg+=(i.find("h3", class_="summary").find("a").string)
                    msg+=("\n")
                    msg+=(description)
                    msg+=("\n")
                    msg+=(str((i.find("div", class_="dateright").find("abbr")["title"].split("T")[0])))
                    msg+=("\n")
                    msg+=(str((i.find("div", class_="dateright").text.strip())))
                    msg+=("\n")
                    msg+=(str(i.find("a", class_="event_item_venue").text).strip())
                    msg+=("\n")
                    pywhatkit.sendwhatmsg_instantly(num,msg)
                    print(msg)
                    msg = ""
                except AttributeError:
                    location = None
        except AttributeError:
            desc = None

