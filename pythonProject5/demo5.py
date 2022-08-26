'''import  re
import requests
url = 'https://movie.douban.com/top250'
headers = {'headers':'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' }
ra = requests.get(url,headers=headers)
page_connect = ra.text
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p clsss="">.*?<br>(?P<year>.*?)&nbsp'
                 r'class="rating_num" property="v:average"(?P<score>.*?)</span>',re.S)
result = obj.finditer(page_connect)
for it in result:
    print(it.group('name'))
    print(it.group("score"))
    print(it.group("year").strip())'''
'''import requests
url='https://movie.douban.com/j/chart/top_list?'
param={
'type': '24',
'interval_id': '100:90',
'action':'',
'start': '0',
'limit':'20',
}
headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
}
resp=requests.get(url=url,params=param,headers=headers)
print(resp.text)'''

