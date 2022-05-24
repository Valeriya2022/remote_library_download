import wget
import requests

URL = "https://www.googleapis.com/books/v1/volumes/GPXJLYd7i2oC"
r = requests.get(url=URL)
download_link = "http://72.21.17.51:15588/do_k_ument/The_Ark/Mega_Folder/Fiction/All_Other_Authors/Harry_Potter-Rowling%2C_J_K-Harry_Potter_and_the_Sorcerer_s_Stone.pdf"
print(download_link)
wget.download(download_link, 'book_4.pdf')