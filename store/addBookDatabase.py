import requests

API_ENDPOINT = "http://10.129.0.217:8000/books"



def add_book_to_database(info):
    data = {"data": info}
    data_mat = {"status": 1}

    try:
        r = requests.post(url=API_ENDPOINT, json=data)
        print(r)
        if r.status_code == 201:
            return True
        else:
            return False

    except:
        return False
