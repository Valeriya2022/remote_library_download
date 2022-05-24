import requests
API_ENDPOINT = "http://10.129.0.217:8000/searched-materials/"


def update_searched_materials(id, status):
    data = {"status": status}

    try:
        r = requests.patch(url=API_ENDPOINT+str(id), json=data)
        if r.status_code == 201:
            return True
        else:
            return False

    except:
        return False
