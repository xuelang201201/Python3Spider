"""进行 URL 解码"""

from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

# https://www.baidu.com/s?wd=壁纸
