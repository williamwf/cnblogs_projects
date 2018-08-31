# ================================================================== #
#                           3-2 RDB Storage                          #
# ================================================================== #

## MySQL
#1 连接
import pymysql

db = pymysql.connect(host='localhost',user='root', password='123456', port=3306)  #connect()方法声明一个连接对象
cursor = db.cursor()      #获得操作游标执行sql语句
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()  #获取第一条数据获取版本号
print('Database version:', data) 
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()     #注意操作完关闭

#2 创建表
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()

#3 插入数据
import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()    #数据库更改后，提交事务
except:
    db.rollback()  #事务回滚，保证数据一致性
db.close()

#但上述插入不能改动，通过构造字典，可以随时传入不同参数
#上述代码优化如下
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
#动态sql语句
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
   if cursor.execute(sql, tuple(data.values())):
       print('Successful')
       db.commit()
except:
    print('Failed')
    db.rollback()
db.close()


#4 更新数据
#同样是用占位符构造SQL，然后传入元组形式的参数，执行excute()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
   cursor.execute(sql, (25, 'Bob'))
   db.commit()
except:
   db.rollback()
db.close()

#考虑重复数据则更新，不存在重复则插入
#以上两部分代码优化合并
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

#5 删除数据
table = 'students'
condition = 'age > 20'

sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()

#6 查询数据
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')

