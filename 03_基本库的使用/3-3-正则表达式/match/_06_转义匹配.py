import re

content = r'(百度)www.baidu.com'
result = re.match(r'\(百度\)www\.baidu\.com', content)
print(result)
# <re.Match object; span=(0, 17), match='(百度)www.baidu.com'>  # 成功匹配到原字符串
