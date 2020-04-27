import socket
import urllib.parse
import urllib.request
import urllib.error

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))  # 爬取整个网页
# print(type(response))  # 输出响应的类型
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# data 参数：data 参数是可选的。如果要添加该参数，需要使用 bytes()方法将参数转化为字节流编码格式的
# 内容，即 bytes 类型。另外，如果传递了这个参数，则它的请求方式就不再是 GET 方式，而是 POST 方式。
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# timeout 参数
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
