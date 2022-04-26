import time
import urllib.request


def connect():
    try:
        urllib.request.urlopen('https://www.google.com/')  # Python 3.x
        return True
    except:
        return False


if __name__ == '__main__':
    while not time.sleep(2):
        print('connected' if connect() else 'no internet!')

