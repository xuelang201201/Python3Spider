import requests


def requests_get():
    r = requests.get('http://httpbin.org/get')
    print(r.text)
    # 如果返回结果为json格式，解析返回结果，得到一个字典格式
    print(type(r.text))
    print(r.json())
    print(type(r.json()))
    # 输出结果
    # <class 'str'>
    # {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org',
    #  'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-5ea71cf2-7f32e4070f1ae6b8a4f741a0'},
    #  'origin': '45.135.186.88', 'url': 'http://httpbin.org/get'}
    # <class 'dict'>


def requests_get_params():
    data = {
        'name': 'germey',
        'age': 22
    }
    r = requests.get("http://httpbin.org/get", params=data)
    print(r.text)


if __name__ == '__main__':
    requests_get()
    # 输出结果：
    # {
    #   "args": {},
    #   "headers": {
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Host": "httpbin.org",
    #     "User-Agent": "python-requests/2.22.0",
    #     "X-Amzn-Trace-Id": "Root=1-5ea71be2-aa1cb1a0cbee6d90712e4f80"
    #   },
    #   "origin": "45.135.186.88",
    #   "url": "http://httpbin.org/get"
    # }
    requests_get_params()
    # 输出结果：
    # {
    #   "args": {
    #     "age": "22",
    #     "name": "germey"
    #   },
    #   "headers": {
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Host": "httpbin.org",
    #     "User-Agent": "python-requests/2.22.0",
    #     "X-Amzn-Trace-Id": "Root=1-5ea71be4-c6a81ae8730eb525c736f3ad"
    #   },
    #   "origin": "45.135.186.88",
    #   "url": "http://httpbin.org/get?name=germey&age=22"
    # }
