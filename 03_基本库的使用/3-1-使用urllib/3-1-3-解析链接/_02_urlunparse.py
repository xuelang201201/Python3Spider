from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']  # 列表类型、元组或者特定的数据类型都可以。
print(urlunparse(data))  # 构造url
