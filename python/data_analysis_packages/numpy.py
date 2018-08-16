# 导入numpy包
import numpy as np 

"""
*****************
一、数组操作
*****************
"""
#创建数组
a = np.array(1, 2, 3)
np.asarray(a, dtype = None, order = None)  #按现有数据创建数组
np.arange(start = 0, stop, step = 1, dtype)

#数组操作
a[1]   #元素访问
len(a) #长度

ndarray.T #转置
np.append(arr, values, axis)  #添加
np.insert(arr, idx, values, axis)
np.split(ary, indices_or_sections, axis)   #分割, 第二项的值为整数则表明要创建的等大小的子数组的数量,是一维数组则表明要创建新子数组的点。
np.delete(arr, values, axis)  #删除
np.unique(arr, return_index, return_inverse, return_counts)  #去重

np.sin(arr)  #三角函数
np.arround(arr)  #四舍五入
np.amin(arr, axis)  #最小值
np.str(arr)    #标准差
np.ceil(arr)   #向下取整  

"""
*****************
二、矩阵操作
*****************
"""
# 创建矩阵
a = np.array([1,2,3],[4,5,6])
a = np.arange(8).reshape(2,4)
# 设置和查看数组元素类型
d = nparray(a, dtype=np.float)
d.type

# 获取矩阵大小
a.shape
a.shape[1]  #某一维
# 矩阵维度
a.ndim
# 调整维度
a.reshape((2,4))

# 访问
a.flat[i]

# 创建0矩阵
a = zeros(5, int8)
a = zeros([2,3])
# 创建1和空矩阵
a = ones()
a = empty()
# 创建对角矩阵
np.diag((1, 2, 3))
# 提取矩阵x对角元素的值
np.diag(x)
# 用函数创建矩阵fromfunction
def func(i):
	return i * 2
 
a = fromfunction(func, (5,))    #一维
a = fromfunction(func, (10,10)) #二维

# 矩阵切片
b[start, stop, step]
# 多维数组切片
b[0, (2:4)]  # 二维数组 b[行号, (起:止)] 
b[2:4, 2:4]  # 行号也可切片
b[: ,3]      #读取第三列,逗号前只有一个冒号，表示所有
b[::2, ::2]  #加步长

#比较矩阵a和b
(a==b).all()  #所有元素
(a==b).any()  #对应元素是否有一个

# tile重复某个数组/矩阵
tile(a, n)
tile(a, (2, 1)) #二维数组

