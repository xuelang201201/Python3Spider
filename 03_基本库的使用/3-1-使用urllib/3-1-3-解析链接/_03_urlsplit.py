from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

# 既可以用属性获取值，也可以用索引来获取。
print(result.scheme, result[0])
