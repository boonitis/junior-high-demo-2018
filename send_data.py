import requests

def send(name):
    payload = {'text': name}

    r = request.post("http://192.168.11.35/", data=payload)
    print(r.text)
