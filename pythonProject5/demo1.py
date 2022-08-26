import re
import requests
headers={"user-agent"
:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}
url="https://movie.douban.com/top250"
resp=requests.get(url,headers=headers)
page_content=resp.text
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
               '(?P<score>.*?)</span>',re.S)
result=obj.finditer(page_content)
for it in result:
    print(it.group("name"))
    print(it.group("year").strip())
    print(it.group("score"))
