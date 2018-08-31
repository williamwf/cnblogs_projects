# ================================================================== #
#                           2-2 BeautifulSoup                        #
# ================================================================== #

#1- 解析器
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')  #通常选择lxml
print(soup.p.string)

#2- 基本使用
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')  #对象初始化
print(soup.prettify())    #调用方法解析 prettify更正格式
print(soup.title.string)  #解析title


#3- 节点选择器
#通过节点，解析对应模块
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)  #string只打印内容部分
print(soup.head)
print(soup.p)

#获取名称
print(soup.title.name)
#获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
#print(soup.p['class'])

"""
> {'class': ['title'], 'name': 'dromouse'}
> dromouse
"""
#获取内容
print(soup.p.string)

#关联选择
#子节点和子孙节点
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)  #contents 获取子节点的列表
print(soup.p.children)  #children 返回的是生成器类型
for i, child in enumerate(soup.p.children):
    print(i, child)
print(soup.p.descendants)  #所有子孙节点
for i, child in enumerate(soup.p.descendants):
    print(i, child)

#父节点和祖先节点
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent) #父节点
print(type(soup.a.parents))  #所有父亲节点
print(list(enumerate(soup.a.parents)))

#兄弟节点
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))


#4- 方法选择器
#4.1 find_all() 
#API
find_all(name , attrs , recursive , text , **kwargs)

#例子
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

##1)name参数
print(soup.find_all(name='ul'))  
print(type(soup.find_all(name='ul')[0]))

#只要返回tag类型，就可以继续查询
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

##2)attrs参数
print(soup.find_all(attrs={'id': 'list-1'})) #参数类型是字典
print(soup.find_all(attrs={'name': 'elements'}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))

##3)text参数
print(soup.find_all(text=re.compile('link'))) #匹配文本

#4.2 find() 匹配一个元素
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

#find_parents()
#find_next_siblings() 
#find_all_next() 

#5- CSS选择器
#select()方法
#返回的结果均是符合CSS选择器的节点组成的列表
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

#嵌套选择
for ul in soup.select('ul'):   
    print(ul.select('li'))   
#获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

#获取文本
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)

