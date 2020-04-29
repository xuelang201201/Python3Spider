import re

# 贪婪匹配
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))
# 输出结果：
# <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
# 7

# 非贪婪匹配
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
# 输出结果：
# <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
# 1234567

# 如果匹配的结果在字符串结尾，.*? 就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符。
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print('result1', result1.group(1))
print('result2', result2.group(1))
# result1
# result2 kEraCN
