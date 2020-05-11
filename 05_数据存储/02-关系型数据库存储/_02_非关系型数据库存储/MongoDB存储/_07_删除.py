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

# 4.删除
result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)
# collection.find_one_and_delete()
# collection.find_one_and_replace()
# collection.find_one_and_update()

# 关于 PyMongo 的详细用法：http://api.mongodb.com/python/current/api/pymongo/collection.html
