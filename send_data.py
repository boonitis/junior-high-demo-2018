from urllib.parse import urlencode
from urllib.request import Request, urlopen

def send(name):
    url = 'https://192.168.11.35' # Set destination URL here
    post_fields = {'text': name}     # Set POST fields here

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)
