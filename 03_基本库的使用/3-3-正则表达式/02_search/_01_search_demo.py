import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match(r'Hello.*?(\d+).*?Demo', content)
print(result)
# 输出结果：None  # match() 方法在使用时需要考虑到开头的内容

result = re.search(r'Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
# <re.Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>
# 1234567
