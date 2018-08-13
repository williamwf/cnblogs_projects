# 版本Python 3.6

####################################################
## 1. 原始数据类型和运算符
####################################################

# 模除
7 % 3 # => 1

# x的y次方
2**4 # => 16

# 格式化字符串
"{} can be {}".format("strings", "interpolated")
#=> "strings can be interpolated"

# 重复参数
"{0} can be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
#=> "Jack be nimble, Jack be quick, Jack jump over the candle stick"


####################################################
## 2. 变量和集合
####################################################

# a. 列表 list
li = [1, 2, 3, 4]
li[2] #访问
li = [1, 3, 4, '456', [1, 2, 3], {1: 'one', 2: 'two'}] #元素可以为不同类型

# 操作
li.append(1)     #最后追加元素
li.pop()         #尾部删除元素
li[始:终:step]    #列表切片
l_a.extend(l_b)  #添加

len(li) #列表长度
# 遍历
for i in li:
    print(i)
for i in range(len(i)):
    print(li[i])

# b. 元组 tuple
# 不可改变的序列
tup = (1, 2, 3)
tup[0]   #访问
tup + (4, 5, 6)    # => (1, 2, 3, 4, 5, 6)
tup[:2]            # => (1, 2)
a, b, c = (1, 2, 3)  # 可以把元组合列表解包，赋值给变量


# c. 字典 dict
# 用字典表达映射关系

# 初始化的字典
d = {'a': 1, 'b' : 2, 1: 'one', 2: 'two', 3: [1, 2, 3]}  #字典是无序的，hash表
print (d)

# 访问元素
d['a']
d[1]

# 字典的遍历
list(d.keys())     # => ["three", "two", "one"]
list(d.values())   # => [3, 2, 1]

for key in d:
    print(d[key])   #遍历值
for key, value in d.items():
	print (key, value)  #遍历键，值

# 字典操作
d.get("one")      # => 1
d.setdefault("five", 5)  # d["five"]设为5
d.update({"four":4}) 
del fd["one"]

# d. 集合 set
s_a = set([1, 2, 2, 3, 4, 5, 5]) #打印时会自动去重，且无序
s_b = set([4, 5, 6, 7, 8, 9])

#判断元素是否存在
5 in s_a

#添加元素
s_a.add(5) 

#并集
s_a | s_b
s_a.union(s_b)
 
#交集
s_a & s_b
s_a.intersection(s_b)

#差集 A - (A&B)
s_a - s_b
s_a.difference(s_b)

#对称差 (A + B) - (A & B)
s_a ^ s_b
s_a.symmetric_difference(s_b)


####################################################
## 3. 流程控制和迭代器
####################################################

# if else条件语句
some_var = 5
if some_var > 10:
    print("some_var比10大")
elif some_var < 10:    # elif句是可选的
    print("some_var比10小")
else:                  # else也是可选的
    print("some_var就是10")

# for循环语句遍历列表
for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

# "range(number)"返回数字列表从0到给的数字
for i in range(4):
    print(i)

# while循环直到条件不满足
x = 0
while x < 4:
    print(x)
    x += 1

# 用try/except块处理异常状况
try:
    # 用raise抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # pass是无操作，但是应该在这里处理错误
except (TypeError, NameError):
    pass    # 可以同时处理不同类的错误
else:   # else语句是可选的，必须在所有的except之后
    print("All good!")   # 只有当try运行完没有错误的时候这句才会运行


####################################################
## 4. 函数
####################################################

# 用def定义新函数
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y    # 用return语句返回

# 调用函数
add(5, 6)   # => 印出"x is 5 and y is 6"并且返回11

# 也可以用关键字参数来调用函数
add(y=6, x=5)   # 关键字参数可以用任何顺序


# 我们可以定义一个可变参数函数
def varargs(*args):
    return args

varargs(1, 2, 3)   # => (1, 2, 3)


# 我们也可以定义一个关键字可变参数函数
def keyword_args(**kwargs):
    return kwargs

# 我们来看看结果是什么：
keyword_args(big="foot", loch="ness")   # => {"big": "foot", "loch": "ness"}


# 这两种可变参数可以混着用
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# 调用可变参数函数时可以做跟上面相反的，用*展开序列，用**展开字典。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)   # 相当于 foo(1, 2, 3, 4)
all_the_args(**kwargs)   # 相当于 foo(a=3, b=4)
all_the_args(*args, **kwargs)   # 相当于 foo(1, 2, 3, 4, a=3, b=4)


# 函数作用域
x = 5

def setX(num):
    # 局部作用域的x和全局域的x是不同的
    x = num # => 43
    print (x) # => 43

def setGlobalX(num):
    global x
    print (x) # => 5
    x = num # 现在全局域的x被赋值
    print (x) # => 6

setX(43)
setGlobalX(6)


def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# 也有匿名函数
(lambda x: x > 2)(3)   # => True

# 内置的高阶函数
map(add_10, [1, 2, 3])   # => [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7])   # => [6, 7]

# 用列表推导式可以简化映射和过滤。列表推导式的返回值是另一个列表。
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]   # => [6, 7]


####################################################
## 5. 模块
####################################################

# 用import导入模块
import math
print(math.sqrt(16))  # => 4.0

# 也可以从模块中导入个别值
from math import ceil, floor
print(ceil(3.7))  # => 4.0
print(floor(3.7))   # => 3.0

# 可以导入一个模块中所有值
# 警告：不建议这么做
from math import *

# 如此缩写模块名字
import math as m
math.sqrt(16) == m.sqrt(16)   # => True

# Python模块其实就是普通的Python文件。你可以自己写，然后导入，
# 模块的名字就是文件的名字。

# 你可以这样列出一个模块里所有的值
import math
dir(math)


