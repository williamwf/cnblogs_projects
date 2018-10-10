##Python登陆网页

from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)

#匹配网页内容- 正则表达式
#查找标题
import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])
#查找段落内容
res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])
#查找链接
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)




