import requests
from bs4 import BeautifulSoup

URL = "https://www.googleapis.com/books/v1/volumes/GPXJLYd7i2oC"
headers = {
    "User-Agent": "PostmanRuntime/7.20.1",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Postman-Token": "8eb5df70-4da6-4ba1-a9dd-e68880316cd9,30ac79fa-969b-4a24-8035-26ad1a2650e1",
    "Host": "medianet.edmond-de-rothschild.fr",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "cache-control": "no-cache",
'Content-type': 'application/pdf'}
r = requests.get(url=URL)
download_link = r.json()["accessInfo"]["pdf"]["downloadLink"]
print(download_link)

# URL from which pdfs to be downloaded
url = "https://demo.codingdiksha.com/embed-pdf-in-html/files/traveldoc.pdf"

# Requests URL and get response object
response = requests.get(download_link, stream=True)

with open("python.pdf", "wb") as pdf:
    for chunk in response.iter_content(chunk_size=1024)
    pdf.write(book.content)
    pdf.close()

