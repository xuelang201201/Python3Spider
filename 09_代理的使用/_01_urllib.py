from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '221.2.175.238:8060'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
# {
#   "args": {},
#   "headers": {
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.8",
#     "X-Amzn-Trace-Id": "Root=1-5ebfcb8f-a6ae943603c0ac36891ed2c2"
#   },
#   "origin": "221.2.175.238",
#   "url": "http://httpbin.org/get"
# }
