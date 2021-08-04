import json
from urllib.request import urlopen
from apikey import apiKey

baseUrl = "https://www.googleapis.com/books/v1/volumes?q="
url = "https://www.googleapis.com/books/v1/volumes?q="

def searchByTitle(title):
   title = title.replace(" ", "+")
   reqUrl = f'{url}{title}&{apiKey}'

   response = urlopen(reqUrl)
   data = json.load(response)

   return data

if __name__ == '__main__':
   title = input("Enter title : ")
   print(searchByTitle(title))