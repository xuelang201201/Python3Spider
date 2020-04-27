"""
该方法可以将内容转化为 URL 编码的格式
"""

from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
