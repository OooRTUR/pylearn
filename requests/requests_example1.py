import requests

URL = 'https://httpbin.org'

def get_request():
    payload = {'page':2, 'count':25}
    r = requests.get(URL+'/get', params=payload)
    print(r.url)

def post_request():
    payload = {'username':'corey', 'password':'testing'}
    r = requests.post(URL+'/post', data=payload)
    print(r.json())

def auth():
    r = requests.get(URL+'/basic-auth/corey/test', auth=('corey','test'))
    print(r.text)
    print(r.status_code)

auth()