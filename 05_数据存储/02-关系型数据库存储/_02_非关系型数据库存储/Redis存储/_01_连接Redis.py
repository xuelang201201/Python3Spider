from redis import StrictRedis, ConnectionPool

redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')
redis.set('name', 'Bob')
print(redis.get('name'))

# 还可以使用 ConnectionPool 来连接
pool = ConnectionPool(host='localhost', port=6379, db=0, password='foobared')
redis = StrictRedis(connection_pool=pool)

# 另外，ConnectionPool 还支持通过 URL 来构建。URL 的格式支持有如下 3 种：
# redis://[:password]@host:posr/db
# rediss://[:password]@host:posr/db
# unix://[:password]@/path/to/socket.sock?db=db
url = 'redis://:foobared@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
