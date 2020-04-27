"""
如果我们有一串 GET 请求参数，利用 parse_qs() 方法，就可以将它转会字典
"""
from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))

# {'name': ['germey'], 'age': ['22']}
