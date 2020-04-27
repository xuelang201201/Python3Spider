import requests

r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
# 保存提取到的图片
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
