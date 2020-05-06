import requests
URL ='https://xkcd.com/353/'

r = requests.get(URL)

print(r)
print(r.text)


URL1 = 'https://imgs.xkcd.com/comics/python.png'

r1= requests.get(URL1)

with open('comic.png', 'wb') as f:
    f.write(r1.content)

print(r1.headers)

