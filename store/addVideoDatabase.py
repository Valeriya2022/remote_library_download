import requests

API_ENDPOINT = "http://10.129.0.217:8000/videos"



def add_video_to_database(info):
    data = {"data": info}

    try:
        r = requests.post(url=API_ENDPOINT, json=data)
        print(r)
        if r.status_code == 201:
            return True
        else:
            return False

    except:
        return False
