import requests

from pyquery import PyQuery as pq

doc = pq(url='https://www.bilibili.com')
print(doc('title'))
# <title>哔哩哔哩 (゜-゜)つロ 干杯~-bilibili</title>

# 等同于
doc = pq(requests.get('https://www.bilibili.com').text)
print(doc('title'))
# <title>哔哩哔哩 (゜-゜)つロ 干杯~-bilibili</title>
