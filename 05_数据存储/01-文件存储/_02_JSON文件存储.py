import json

"""读取 JSON"""
s = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(s))
data = json.loads(s)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))

with open('data.json', 'r') as file:
    s = file.read()
    data = json.loads(s)
    print(data)

"""输出 JSON"""
data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))  # 保存格式

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
