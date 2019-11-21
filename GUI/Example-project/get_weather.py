import requests


def run(url):
    try:
        rep = requests.get(url)
        rep.encoding = 'utf-8'
        return rep
    except:
        print("network error")