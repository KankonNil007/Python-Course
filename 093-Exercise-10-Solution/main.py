# Exercise 10 - Solution

import requests

def func1(categ):
    url = (f'https://newsapi.org/v2/top-headlines?category={categ}&pageSize=5&apiKey=defa8240238044509487b054a23f9d00')

    response = requests.get(url)
    data = response.json()

    for i, article in enumerate(data["articles"], start=1):
        print(f"--- Article - {i} ---")
        print(f"Source: {article['source']['name']} (ID: {article['source']['id']})")
        print(f"Published: {article['publishedAt']}")
        print(f"Author: {article['author']}\n")
        print(f"Title: {article['title']}\n")
        print(f"Description: {article['description']}\n")
        print(f"URL: {article['url']}")
        print("-----------------------------------------")
        print("\n")

def func2(srchTpc):
    url = (f'https://newsapi.org/v2/everything?q={srchTpc}&pageSize=5&apiKey=defa8240238044509487b054a23f9d00')

    response = requests.get(url)
    data = response.json()

    for i, article in enumerate(data["articles"], start=1):
        print(f"--- Article - {i} ---")
        print(f"Source: {article['source']['name']} (ID: {article['source']['id']})")
        print(f"Published: {article['publishedAt']}")
        print(f"Author: {article['author']}\n")
        print(f"Title: {article['title']}\n")
        print(f"Description: {article['description']}\n")
        print(f"URL: {article['url']}")
        print("-----------------------------------------")
        print("\n")

def searchTopic():
    inpTopic = input("Enter your Keyword: ")
    func2(inpTopic)
    print("\n")
    choiceList()

def categoryList(categ):
    func1(categ)
    print("\n")
    choiceList()

def screenView():
    print("Welcome to News - Categories")
    print("1.Search Topics")
    print("2.Business")
    print("3.Entertainment")
    print("4.General")
    print("5.Science")
    print("6.Sports")
    print("7.Technology")
    print("8. Exit")

def choiceList():
    inpChoice = int(input("Enter your Choice:"))

    if (inpChoice == 1):
        searchTopic()
    elif (inpChoice == 2):
        categoryList("business")
    elif (inpChoice == 3):
        categoryList("entertainment")
    elif (inpChoice == 4):
        categoryList("general")
    elif (inpChoice == 5):
        categoryList("science")
    elif (inpChoice == 6):
        categoryList("sports")
    elif (inpChoice == 7):
        categoryList("technology")
    elif (inpChoice == 8):
        print("Program Ended Successfully!!")
    else:
        print("Invalid Choice!!\n")
        choiceList()

screenView()
choiceList()