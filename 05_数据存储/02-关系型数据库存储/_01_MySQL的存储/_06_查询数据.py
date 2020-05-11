import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

# sql = 'SELECT * FROM students WHERE name LIKE "Bob"'
# sql = 'SELECT * FROM students WHERE age = 21'
# sql = 'SELECT * FROM students WHERE age = 21 AND name LIKE "Mary"'
# sql = 'SELECT * FROM students WHERE age = 21 OR age = 20'
sql = 'SELECT * FROM students WHERE age > 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    # one = cursor.fetchone()
    # print('One:', one)
    # results = cursor.fetchall()  # 如果数据量很大，占用的开销会非常高。
    # print('Results:', results)
    # print('Results Type:', type(results))
    # for row in results:
    #     print(row)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except Exception as reason:
    print('Error: ' + str(reason))

db.close()
