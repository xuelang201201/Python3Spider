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

# 4.计数
# count = collection.find({'age': 20}).count()
count = collection.count_documents({'age': 20})
print(count)
