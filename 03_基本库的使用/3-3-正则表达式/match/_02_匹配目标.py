import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^Hello\s(\d+)\sWorld', content)  # 使用 () 括号将想提取的子字符串括起来。
print(result)
print(result.group())
print(result.group(1))  # 调用 group() 方法传入分组的索引即可获取提取的结果。第一个被()包围的匹配结果。
print(result.span())
