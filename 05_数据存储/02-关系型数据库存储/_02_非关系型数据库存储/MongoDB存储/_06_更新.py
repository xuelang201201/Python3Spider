import pymongo

# 1.连接 MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')  # 也可以直接传入

# 2.指定数据库
db = client.test
# db = client['test']  # 两种方式是等价的

# 3.指定集合
collection = db.students
# collection = db['students']

# 4.更新
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)  # 匹配的数据条数，影响的数据条数

condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})  # 将第一条符合条件的年龄加 1
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})  # 将所有符合条件的数据都更新
print(result)
print(result.matched_count, result.modified_count)
