import redis


# 连接数据库
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# 创建3 条数据
person1 = {
'name': '刘硕',
'age': 34,
'sex': 'M',
}

person2= {
'name': '李雷',
'age': 32,
'sex': 'M',
}

person3= {
'name': '韩梅梅',
'age': 31,
'sex': 'F',
}

r.hmset('person:1', person1)
r.hmset('person:2', person2)
r.hmset('person:3', person3)

# 关闭连接 
r.connection_pool.disconnect()