from store.searchDownloadBook import search_download_book
from store.addBookDatabase import add_book_to_database
from store.updateSearchedMaterials import update_searched_materials
from store.searchDownloadVideo import search_download_video
from store.addVideoDatabase import add_video_to_database


def download_all_materials(search_materials, path_book, path_video):
    for material in search_materials:
        if material["category"] == "book":
            info = search_download_book(material["query"], path_book, material["id"])
            print(info)
            if info:
                res = add_book_to_database(info)
                if res:
                    update_searched_materials(material["id"], 1)
            else:
                update_searched_materials(material["id"], -1)
        if material["category"] == "video":
            info = search_download_video(material["query"], path_video, material["id"])
            if info:
                print(info)
                a = add_video_to_database(info)
                if a:
                    print("successfully added to database")
                    update_searched_materials(material["id"], 1)
                else:
                    update_searched_materials(material["id"], -1)
        if material["category"] == "all":
            info_video = search_download_video(material["query"], path_video, material["id"])
            if info_video:
                print(info_video)
                a = add_video_to_database(info_video)
                if a:
                    print("successfully added to database")
                    update_searched_materials(material["id"], 1)
                else:
                    update_searched_materials(material["id"], -1)
            info_book = search_download_book(material["query"], path_book, material["id"])
            print(info_book)
            if info_book:
                res = add_book_to_database(info_book)
                if res:
                    update_searched_materials(material["id"], 1)
    return True



