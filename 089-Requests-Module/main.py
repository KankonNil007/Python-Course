# Requests Module in Python

import requests

response = requests.get("https://kankonnil007.github.io") # Selects a destination 

print(response.text) # Prints out the source code of a webpage

# Post Method in Requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Kankon",
    "body": "Nil",
    "userID": 23
}

headers = {
    "Content-type": "application/json; charset=UTF-8"
}

response2 = requests.post(url, headers=headers, json=data)

print(response2.text)

# How to get all h2 tags from a webpage(Web Scraping)

import requests
from bs4 import BeautifulSoup

url = "https://kankonnil007.github.io"
req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

print(soup.prettify()) # Provides you with a source code with proper indentation

for h in soup.find_all("h2"):
    print(h.text)