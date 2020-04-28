"""
假设莫个网站需要认证
如果认证成功，返回 200 状态码
失败，返回 401。
"""

import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

# 直接传入一个元组，它会默认使用 HTTPBasicAuth 这类来认证。
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)

# OAuth 认证
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
