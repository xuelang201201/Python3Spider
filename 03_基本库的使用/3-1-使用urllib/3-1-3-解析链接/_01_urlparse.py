from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

"""
http://www.baidu.com/index.html;user?id=5#comment

 urlparse()方法将其拆分成了6个部分。大体观察可以发现，解析时有特定的分隔符。比如，
://前面的就是 scheme，代表协议；第一个/符号前面便是 netloc，即域名，后面是 path，
即访问路径；分号;后面是 params，代表参数；问号?后面是查询条件query，一般用作 GET
类型的 URL；井号#后面是锚点，用于直接定位页面内部的下拉位置。
    所以，可以得出一个标准的链接格式，具体如下：
    scheme://netloc/path;params?query#fragment
"""
