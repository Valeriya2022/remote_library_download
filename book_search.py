import requests
import urllib.request

URL = "https://www.googleapis.com/books/v1/volumes?q=stranger&filter=free-ebooks&orderBy=relevance&download=epub"
proxies = {"http": "http://10.10.1.10:3128",
           "https": "http://10.10.1.10:1080"}

r = requests.get(url=URL)
a = r.json()['items']
i = 0
j = 0
while (i < 3 and j < len(a)):
    if (a[j]['accessInfo']['epub']['isAvailable'] == True):
        download_link = a[j]['accessInfo']['epub']['downloadLink']
        print(a[j])
        i += 1
    elif (a[j]['accessInfo']['pdf']['isAvailable'] == True):
        download_link = a[j]['accessInfo']['pdf']['downloadLink']
        print(a[j])
        i += 1
    j += 1

