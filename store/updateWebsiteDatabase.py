import requests
API_ENDPOINT = "http://10.129.0.217:8000/governmental-resource/"


def update_website_database(id):
    data = {}

    try:
        r = requests.patch(url=API_ENDPOINT+str(id), json=data)
        print(r)
        if r.status_code == 201:
            return True
        else:
            return False

    except:
        return False
