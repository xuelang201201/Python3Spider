import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
# 输出结果：
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "age": "22",
#     "name": "germey"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "18",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0",
#     "X-Amzn-Trace-Id": "Root=1-5ea72842-bb6c53fe63e07ef942160a40"
#   },
#   "json": null,
#   "origin": "45.135.186.88",
#   "url": "http://httpbin.org/post"
# }
