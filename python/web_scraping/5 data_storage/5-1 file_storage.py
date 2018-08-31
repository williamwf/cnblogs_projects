# ================================================================== #
#                           3-1 File Storage                         #
# ================================================================== #

#1 txt文本存储
#基本实例- 知乎发现热门问题
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
#读写文件
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    
    file = open('explore.txt', 'a', encoding='utf-8') #a代表以追加的方式写入文本
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

#2 Json存储
#json对象
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
     "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]

#读取
import json

str = '''
[{
    "name": "Bob",          #json对象要用双引号
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

#输出
import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data，indent=2, ensure_ascii=False))  #两格缩进


#3 csv存储
#写入
import csv

with open('data.csv', 'w') as csvfile:  #a为追加写入
    writer = csv.writer(csvfile, delimiter=' ')
    # writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['10001', 'Mike', 20])
    # writer.writerow(['10002', 'Bob', 22])
    # writer.writerow(['10003', 'Jordan', 21])
    writer.writerow(['id', 'name', 'age'])
    # fieldnames = ['id', 'name', 'age']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])


#读取
import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

import pandas  as pd
df = pd.read_csv('data.csv')
print(df)

