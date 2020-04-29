import re

content1 = '2020-4-29 10:40'
content2 = '2020-4-30 10:55'
content3 = '2020-5-1 13:21'
pattern = re.compile(r'\d{2}:\d{2}')  # 将正则表达式编译成一个正则表达式对象，以便复用。
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
# 2020-4-29  2020-4-30  2020-5-1
