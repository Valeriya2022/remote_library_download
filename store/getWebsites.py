import requests
import datetime
from dateutil.parser import parse

def get_websites(IP_ADDRESS):
    try:
        URL = "http://"+IP_ADDRESS+":8000/governmental-resource"
        r = requests.get(url=URL)
        new_data = []
        data = r.json()
        for web in data:
            now = datetime.date.today()
            now = now.strftime("%Y-%m-%d")
            now = parse(now)
            date1 = parse(web["update_date"])
            if (now - date1) > datetime.timedelta(7):
                new_data.append(web)

        return new_data
    except Exception:
        return False
