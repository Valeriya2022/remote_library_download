import requests


def get_searched_materials(IP_ADDRESS):
    try:
        URL = "http://"+IP_ADDRESS+":8000/searched-materials"
        r = requests.get(url=URL)
        data = r.json()
        return data
    except Exception:
        return False

