# ================================================================== #
#                           2-1 Xpath                                #
# ================================================================== #

#自动补齐标签
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser()) #etree对文本进行自动修正
result = etree.tostring(html)  #输出代码
print(result.decode('utf-8'))

#先自定义一个文件
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

#操作
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//*')     # //*  选择所有节点
result = html.xpath('//li')    #选择性获取
result = html.xpath('//li/a')  #/ 选择子节点（指定）
result = html.xpath('//ul//a') #//所有子孙节点
result = html.xpath('//a[@href="link4.html"]/../@class')  #..父节点  @class属性
result = html.xpath('//li[@class="item-0"]/text()')   #text() 获取节点中的文本
result = html.xpath('//li[@class="item-0"]/a/text()') #获取节点内部文本，留意节点格式
result = html.xpath('//li[@class="item-0"]//text()')  #获取子孙节点的所有文本

result = html.xpath('//li/a/@href')  #属性获取
result = html.xpath('//li[@class="li"]/a/text()')   #属性匹配
result = html.xpath('//li[contains(@class, "li")]/a/text()')  #属性多值匹配
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()') #多属性地图

#按位置选择
result = html.xpath('//li[1]/a/text()')  #第一个li节点
result = html.xpath('//li[last()]/a/text()')  #最后一个
result = html.xpath('//li[position()<3]/a/text()')  #前三个
result = html.xpath('//li[last()-2]/a/text()') #倒数


print(result)   # 取结果是一个列表形式，其每一个元素都是一个 Element 对象，可通过索引调用

