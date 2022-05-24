import requests
import datetime
from dateutil import parser


def delete_not_accessed_materials(IP_ADDRESS, path_book, path_video):
    td = datetime.timedelta(90)
    now = parser.parse(str(datetime.datetime.now()))
    try:
        new_data = []
        URL = "http://"+IP_ADDRESS+":8000/books"
        r = requests.get(url=URL)
        data = r.json()
        print(data)
        for book in data:
            # book_time = parser.parse(book["last_visited_date_time"].replace("Z", ""))
            book_time = parser.parse(book["last_visited_date_time"].replace("Z", ""))

            if (now-book_time) > td:

                try:
                    r = requests.delete("http://"+IP_ADDRESS+":8000/books/"+str(book["id"]))
                    new_data.append(book)
                except:
                    print("could not delete")

        print("successfully deleted unused book", new_data)

    except Exception:
        print("failes")
        return False

    try:
        new_data = []
        URL = "http://"+IP_ADDRESS+":8000/videos"
        r = requests.get(url=URL)
        data = r.json()
        print(data)
        for book in data:
            # book_time = parser.parse(book["last_visited_date_time"].replace("Z", ""))
            book_time = parser.parse(book["last_visited_date_time"].replace("Z", ""))

            if (now-book_time) > td:

                try:
                    r = requests.delete("http://"+IP_ADDRESS+":8000/videos/"+str(book["id"]))
                    new_data.append(book)
                except:
                    print("could not delete videos")

        print("successfully deleted unused videos", new_data)

    except Exception:
        print("failes")
        return False

