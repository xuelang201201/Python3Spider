import requests

# r = requests.get("https://www.taobao.com", timeout=1)  # 连接（connect）和读取（read）的 timeout 总和。
# r = requests.get("https://www.taobao.com", timeout=(5, 30))  # 分开设置
# r = requests.get("https://www.taobao.com", timeout=None)  # 永久等待
r = requests.get("https://www.taobao.com")  # 永久等待
print(r.status_code)
