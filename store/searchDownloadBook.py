import requests
import wget


def search_download_book(query, path, mat_id):
    url = "https://filepursuit.p.rapidapi.com/"
    querystring = {"q": query, "type": "ebook"}
    info = []

    headers = {
        "X-RapidAPI-Host": "filepursuit.p.rapidapi.com",
        "X-RapidAPI-Key": "9098f7e6d0msh8a50e0dff56f3bbp168c21jsn834cdd902d49"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.json()['status'] == "success":
        print("books_were_found")
        i = 0
        j = 0
        names = []
        files = response.json()["files_found"]
        while i < 3 and j < len(files):
            if files[j]['file_type'] == 'PDF' or files[j]['file_type'] == 'EPUB':
                download_link = response.json()['files_found'][j]['file_link']
                try:
                    name = "book"+str(query)+str(mat_id)
                    if files[j]['file_type'] == 'PDF':
                        name += ".pdf"
                    elif files[j]['file_type'] == 'EPUB':
                        name += ".epub"
                    name = name.replace(" ", "")

                    if (name not in names):
                        wget.download(download_link, path+name)
                        print("The book was successfully downloaded" +name)
                        i+=1
                        names.append(name)
                        book_info = {"name": files[j]["file_name"][:-4],
                                     "description": "",
                                     "source": "FilePursuit",
                                     "path": "http://10.129.0.217:4000/books/"+name,
                                     "url": download_link,
                                     "publish_year": int(files[j]["date_added"].split("-")[0]),
                                     "book_category": 5}
                        info.append(book_info)

                except:
                    print("could not download")
            j+=1
        return info

    # i = 0
    # j = 0
    # while i < 3 and j < len(response.json()["files_found"]):
    # 	if response.json()['files_found'][j]['file_type'] == 'PDF' or response.json()['files_found'][j]['file_type'] == 'EPUB':
    # 		print(response.json()['files_found'][j])
    # 		download_link = response.json()['files_found'][j]['file_link']
    # 		print(download_link)
    # 		try:
    # 			name = response.json()['files_found'][j]['file_name']
    # 			wget.download(download_link,path+name)
    # 			print("The book was successfully downloaded")
    # 			i+=1
    # 		except:
    # 			print("could not download")
    # 	j+=1
# print(response.text)
