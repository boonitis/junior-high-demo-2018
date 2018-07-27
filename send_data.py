import requests

def send(name):
    payload = name

    r = requests.post("http://192.168.11.35/", data=payload)
    print(r.text)
