import requests
import json
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
soup.prettify()
titles = soup.find_all(class_="title is-5")
companies = soup.find_all(class_="title is-2")
linkTable= []
results = []
links=soup.find_all('a', string="Apply")
for link in links:
    link_url=link["href"]
    linkTable.append(link_url)
for element in linkTable:
    url=element
    web = requests.get(url)
    preetyWeb = BeautifulSoup(web.content, "html.parser")
    title = preetyWeb.find(class_="is-2")
    company = preetyWeb.find(class_="is-4")
    location = preetyWeb.find(id="location")
    posted = preetyWeb.find(id="date")
    description = preetyWeb.find(class_="content")
    slownik = ({"link":url,"title":title.text,"company":company.text,"location":location.text[10:],"posted":posted.text[8:],"description":description.text })
    results.append(slownik)
with open("wyniki.txt",'w') as jsonfile:
    json.dump(results,jsonfile)