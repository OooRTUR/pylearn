import urllib.request

response = urllib.request.urlopen('https://httpbin.org/get')

print(response.read())

print(response.getcode())

youtuberesponse = urllib.request.urlopen('https://www.youtube.com/')

print(youtuberesponse.read())