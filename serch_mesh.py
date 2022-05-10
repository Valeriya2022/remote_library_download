import requests
import wget
from PyPDF2 import PdfFileReader
import os

url = "https://filepursuit.p.rapidapi.com/"

querystring = {"q":"harry potter","type":"ebook"}
path = "C:/Users/valeriya.nikiforova/Documents/UCA\Senior/FYP/remote_library_static_server/books/"

headers = {
	"X-RapidAPI-Host": "filepursuit.p.rapidapi.com",
	"X-RapidAPI-Key": "9098f7e6d0msh8a50e0dff56f3bbp168c21jsn834cdd902d49"
}
def checkFile(fullfile):
    with open(fullfile, 'rb') as f:
        try:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            if info:
                return True
            else:
                return False
        except:
            return False

response = requests.request("GET", url, headers=headers, params=querystring)
if response.json()['status'] == "success":
	print("success")

	i = 0
	j = 0
	while i < 3 and j < len(response.json()["files_found"]):
		if response.json()['files_found'][j]['file_type'] == 'PDF' or response.json()['files_found'][j]['file_type'] == 'EPUB':
			print(response.json()['files_found'][j])
			download_link = response.json()['files_found'][j]['file_link']
			print(download_link)
			try:
				name = response.json()['files_found'][j]['file_name']
				wget.download(download_link,path+name)
				i+=1
			except:
				print("could not download")
		j+=1
# print(response.text)


import requests

url = "https://filepursuit.p.rapidapi.com/"
querystring = {"q":"<REQUIRED>","type":"ebook"}
headers = {
	"X-RapidAPI-Host": "filepursuit.p.rapidapi.com",
	"X-RapidAPI-Key": "9098f7e6d0msh8a50e0dff56f3bbp168c21jsn834cdd902d49"
}
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)