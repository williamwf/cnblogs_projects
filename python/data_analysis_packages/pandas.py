# 导入pandas包
import pandas as pd

#1 DataFrame基本操作
# 创建6*4的随机矩阵
df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))

df.dtypes             #类型
df.head(3)            #前三行
df.tail(5)            #后五行
df.describe()         #描述性统计
df.T                  #转置
df.sort(columns='C')  #按C列排序
df.iloc[1:3, :]       #数据切片

#2 筛选数据
df[(df.D>0) & (df.C<0)]                   #多个关系筛选
df[['A','B']][(df.D>0) & (df.C<0)]   #只返回特定列结果

#3 读取csv数据
os.getcwd()     #获取当前工作目录
df = pd.read_csv('self/…', engine='python', encoding='gbk') #读取文件

#4 数据选择
df[u'专业名称' u'学号'][:3]  #前三行数据

#5 数据统计
counts=df[u'专业名称'].value_counts()  #结果会打印出选择列及对应值 

#6 数据分组
#创建数据
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one','one','three','one','two','one','one','three'], 'C':np.random.randn(8), 'D':np.random.randn(8)})

#分组
grouped = df.groupby(['A', 'B'])
print (gourped.last())  #打印最后一行

#按函数分组
def get_type(letter):
	if letter.lower() in 'abem': 		
                return 'vowel'
	else:
		return 'consonant'

grouped = df.groupby(get_type, axis = 1)
print (grouped.first())

#7 transformation 标准化数据
#将一列数据转换为以1为标准差以0为平均数的标准分数

#创建series对象，以时间戳为index
index = pd.date_range('1/1/2014', periods=100)
ts=pd.Series(np.random.normal(0.5, 2, 100),index)

key = lambda x: x.month       #按月分组
zscore = lambda x: (x-x.mean())/x.std()

transformed =ts.groupby(key).transform(zscore)

print(transformed.groupby(key).mean())
print(transformed.groupby(key).std())

#8 agg分组多种计算
#先创建一个DataFrame
import numpy as np
import pandas.util.testing as tm

colors=tm.np.random.choice(['red','green'],size=10)
foods=tm.np.random.choice(['egg','ham'],size=10)

index=pd.MultiIndex.from_arrays([colors, foods],names=['color','food'])
df=pd.DataFrame(np.random.randn(10,2), index=index)
df.columns = ['a','b']


grouped = df.groupby(level='color')

#计算各组的总数，平均数，标准差
print (grouped.agg([np.sum, np.mean, np.std]))

grouped['a'].agg([np.sum, np.me..  #针对a列计算
grouped['a'].agg({'SUM result': np.sum, 'Mean result': np.mean ..})                                       #自设列标题
grouped['a'].agg({'lambda': lambda x: np.mean(abs(x))})  #通过lambda匿名函数

#9 按月分组
key = lambda x:x.month
grouped = ts.groupby(key)

df=pd.DataFrame({'date':date, 'data':data})
print(df.groupby(df['date'].apply(lambda x:x.month)))  #按日期格式分组并设置列名

#10 字符串日期转Date
date_stngs = (…)
a = pd.Series([pd.to_datetime(date) for date in date_stngs])

#11 移动、复制、删除列
df['c'] = pd.Series(np.random.randn(10), index=df.index)  #增加列
df.insert(1, 'e', df['a'])  #插入列 （位置，列名，值）
df = df.drop(['a', 'b'], axis = 1)  #丢到某列

b = df.pop('b')
df.insert(0, 'b', b)   #移动列

#12 Series 创建带索引数据
ser1 = Series([1,2,3,4])   #默认索引
ser2 = Series(range(4),index = ["a","b","c","d"])    #自定义索引

ser3 = Series({'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000})    #用字典创建

可以通过索引访问值，也可通过ser.values/index 获取所有值/索引

#13 字符串操作
s = pd.Series(list('ABCDEF'))   
print (s)

#同普通字符串操作一样
s.str.upper()
s.str.len()
s.str.split('_')
s.str.replace('^a|b$', 'X', case=False)

s.str.extract('()()')     #字符串提取，每个括号代表一个条件
s.str.contains(条件, na = False)           #包含字符串
s.str.match(条件，as_indexer=False)  #匹配字符串
startswith, endwith…

#14 读写sql数据库
#read_sql接受两个参数，一个是sql语句；一个是con（数据库连接）、read_sql直接返回一个DataFrame对象
con = sqlite3.connect("xx.sqlite") 
sql = "select * from weather_2012 LIMIT 3"
df = pd.read_sql(sql, con, index_col='id')  #将index_col值设置为列表

#写数据
con2 = sqlite3.connect("xx.sqlite") 
con2.execute(“drop table if exists weather_2012”)
pd.io.sql.write_frame(df, “weather_2012”, con2)

#15 广播
对矩阵中每个元素执行相同的操作
df = pd.DataFrame({'one':pd.Series(np.random.randn(4), index=list('abcd'))})
df['two']=1
df['thr']=2

#得到一行和一列
row=df.ix[1]      #ix[1, :-1] 
columns = df['two']

#将df中每一行与row做减法
print(df.sub(row, axis='columns'))  #axis指定广播的纬度

#16 缺失值计算
#简单运算中，运算后相应位置也是缺失的；
df.fillna(0)  #0值填充，也可以用字符串等填充
df.fillna(method='bfill', limit=1)  #后面值填充
df.fillna(df.mean())   #均值填充
df.fillna(df.mean()['one', 'two'])  #指定列填充
df.interpolate()   #插值法估计缺失值  默认直线  #method='values'/'time', 会根据df的类型来自动估计

df.dropna(axis =0)  #删除缺失值的行  axis=1为删除列

#17 值替换
ser = pd.Series([0,1 …])
ser.replace(0, 6)
ser.replace({1:11, 2:12})  #字典映射

#同样适用于df对象
df[['a', 'b']].replace(2, 10)  #指定多列进行替换
#若多个列中不同的值都要替换为一个相同的值，可以使用字典的方法表示所有需要被替换的值：
df.replace({'a':0, 'b':5}, np.nan)


