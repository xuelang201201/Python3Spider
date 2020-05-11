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

# 4.偏移
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)  # 忽略前两个元素
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)  # 忽略前两个元素，并且只取前两个结果
print([result['name'] for result in results])
# ['Kevin', 'Mike', 'Sarah']
# ['Kevin', 'Mike']
# 当数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，容易导致内存溢出。
results = collection.find({'_id': {'$gt': ObjectId('5eb986e5bfcd594cd2a8870e')}})
print([result for result in results])
