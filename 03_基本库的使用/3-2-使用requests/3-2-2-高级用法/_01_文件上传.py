import requests,os

files = {'file': open('../3-2-1-基本用法/favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
