import pymysql

data = {
    'id': '20120001',
    'user': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(['%s'] * len(data))
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()



