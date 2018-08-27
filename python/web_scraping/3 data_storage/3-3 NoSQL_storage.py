# ================================================================== #
#                           3-2 NoSQL Storage                          #
# ================================================================== #
## MongoDB
#1 连接
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
#client = MongoClient('mongodb://localhost:27017/')

#2 指定数据库
db = client.test

#3 指定集合
#类似RDB中的表
collection = db.students

#4 插入数据
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result)   #每条数据会有唯一一个_id属性来标识

#5 查询find_one() 或 find_all()
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

#6 更新
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

result = collection.update(condition, {'$set': student})  #只更新student内存在字段
#update_one() 和 update_many()

#7 删除
result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)

