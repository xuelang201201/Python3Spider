import pymysql

db = pymysql.connect(host='localhost', user='debian-sys-maint', password='k2guMUXboBU0V3jk', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
