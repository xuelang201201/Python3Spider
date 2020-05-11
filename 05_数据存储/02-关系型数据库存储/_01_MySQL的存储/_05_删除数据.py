import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    print('Successful')
    db.commit()
except Exception as reason:
    # print('Failed: ' + str(reason))
    db.rollback()

db.close()
