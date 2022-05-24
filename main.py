import time
import urllib.request
from store.getMaterials import get_searched_materials
from store.searchAllMaterials import download_all_materials
from store.update_website import update_website
from store.getWebsites import get_websites
from store.updateWebsiteDatabase import update_website_database
from store.getNotAccessedMaterials import delete_not_accessed_materials

IP_ADDRESS = "10.129.0.217"
PATH_BOOK = "C:/Users/valeriya.nikiforova/Documents/UCA\Senior/FYP/remote_library_static_server/books/"
PATH_VIDEO = "C:/Users/valeriya.nikiforova/Documents/UCA\Senior/FYP/remote_library_static_server/videos/"
PATH_WEB = "C:/Users/valeriya.nikiforova/Documents/UCA\Senior/FYP/remote_library_static_server/governmental_resources"


def connect():
    try:
        urllib.request.urlopen('https://www.google.com/')  # Python 3.x
        return True
    except:
        return False


if __name__ == '__main__':
    t = 2
    while not time.sleep(t):
        print('connected' if connect() else 'no internet!')
        materials_to_download = []
        if connect():
            searched_materials = get_searched_materials("10.129.0.217")
            if searched_materials:
                t = 1800
                for material in searched_materials:
                    if material["status"]==0:
                        materials_to_download.append(material)
            print(materials_to_download)
            download_all_materials(materials_to_download, PATH_BOOK, PATH_VIDEO)
            websites = get_websites(IP_ADDRESS)
            print(websites)
            if websites and len(websites) > 0:
                for website in websites:
                    update_website(website["source"], PATH_WEB, website["url"])
                    res = update_website_database(website["id"])
                    if res:
                        print("successfully")


        else:
            delete_not_accessed_materials(IP_ADDRESS, PATH_BOOK, PATH_VIDEO)
            t = 30






