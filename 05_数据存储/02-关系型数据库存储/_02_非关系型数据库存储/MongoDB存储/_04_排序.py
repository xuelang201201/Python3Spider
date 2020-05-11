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

# 4.排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])
# ['Harden', 'Jordan', 'Kevin', 'Mike', 'Sarah']
