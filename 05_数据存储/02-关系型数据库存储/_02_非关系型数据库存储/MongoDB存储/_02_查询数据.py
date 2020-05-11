import pymongo

from bson.objectid import ObjectId

# 1.连接 MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')  # 也可以直接传入

# 2.指定数据库
db = client.test
# db = client['test']  # 两种方式是等价的

# 3.指定集合
collection = db.students
# collection = db['students']

# 4.查询数据
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)
# 根据 ObjectId 查询
result = collection.find_one({'_id': ObjectId('5eb986e5bfcd594cd2a8870c')})
print(result)
# 查询多条数据
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)
# 查询大于 20 岁的数据
"""
                        比较符号
————————————————————————————————————————————————————————————
    符号         含义                   实例
————————————————————————————————————————————————————————————
    $lt         小于            {'age': {'$lt': 20}}
    $gt         大于            {'age': {'$gt': 20}}
    $lte        小于等于        {'age': {'$lt': 20}}
    $gte        大于等于        {'age': {'$gte': 20}}
    $ne         不等于          {'age': {'$ne': 20}}
    $in         在范围内        {'age': {'$in': [20, 23]}}
    $nin        不在范围内      {'age': {'$nin': [20, 23]}}
——————————————————————————————————————————————————————————————
"""
results = collection.find({'age': {'$gt': 20}})
print(results)
for result in results:
    print(result)
# 查询名字以 M 开头的学生数据
"""
                                            功能符号
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
符 号         含   义                 示   例                                              示例含义
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
$regex      匹配正则表达式     {'name': {'$regex': '^M.*'}}                           name 以 M 开头
$exists     属性是否存在       {'name': {'$exists': True}}                            name 属性存在
$type       类型判断           {'age': {'$type': 'int'}}                              age 的类型为 int
$mod        数字模操作         {'age': {'$mod': [5, 0]}}                              年龄模 5 余 0
$text       文本查询           {'$text': {'$search': 'Mike'}}                         text 类型的属性中包含 Mike 字符串
$where      高级条件查询       {'$where': 'obj.fans_count == obj.follows_count'}      自身粉丝数等于关注数
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
results = collection.find({'name': {'$regex': '^M.*'}})
print(results)
for result in results:
    print(result)
