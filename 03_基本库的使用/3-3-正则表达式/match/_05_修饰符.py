import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match(r'^He.*?(\d+).*?Demo$', content, re.S)  # re.S修饰符的作用是让 . 匹配包括换行符在内的所有字符。
print(result.group(1))
# 不加 re.S 的运行结果：
# Traceback (most recent call last):
#   File "_05_修饰符.py", line 7, in <module>
#     print(result.group(1))
# AttributeError: 'NoneType' object has no attribute 'group'
