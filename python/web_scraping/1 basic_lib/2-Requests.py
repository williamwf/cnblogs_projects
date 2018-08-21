"""
################
I 基本使用
################
"""
### 1.1 实例引入

import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')


### 1.2 GET请求
import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

# params添加参数
import requests

data = {
    'name': 'germey',
    'age': 22
}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)

# r.json() 返回为字典类型
import requests

r = requests.get("http://httpbin.org/get")
print(type(r.text))
print(r.json())
print(type(r.json()))

#添加header信息抓取网页
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)


#抓取二进制数据（图片，音频，视频）
import requests

r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
#存储数据
with open('favicon.ico', 'wb') as f:
    f.write(r.content)


### 1.3 POST请求
import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)

#返回中，form部分就是提交的数据

### 1.4 Response
import requests

r = requests.get('http://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

"""
################
II 高级用法
################
"""
# 2.1- 文件上传
import requests

files = {'file': open('favicon.ico', 'rb')}  #文件和当前脚本同一目录
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

# 2.2- Cookies
import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

# 替换成你自己的 Cookies，将其设置到 Headers 里面，发送 Request，
import requests
headers = {
    'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)

# 2.3- SSL证书验证
import requests
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


# 2.4- 代理设置
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080', #无效
  #'https': 'http://user:password@10.10.1.10:3128/', HTTP Basic Auth要求
}

requests.get('https://www.taobao.com', proxies=proxies)

# 2.5- 超时设置
import requests

r = requests.get('https://www.taobao.com',timeout=(5, 11)) # connect（连接）和 read（读取）
print(r.status_code)

# 2.6- 身份认证
import requests

r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)

## 2.7- Prepared Request
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

"""
################
III 正则表达式
################
"""

#3.1- match()

#匹配文字
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
result = re.match('^Hello.*Demo$', content)  #通用匹配
result = re.match('^He.*?(\d+).*Demo$', content)  #非贪婪策略提取数字
result = re.match('^He.*?(\d+).*?Demo$', content, re.S) #针对换行符

print(result)
print(result.group())  #分组
print(result.group(1)) #对象访问
print(result.span())

#3.2- search()









