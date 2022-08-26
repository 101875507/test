import requests
import re
url="http://www.wangwenba.cn/"
headers={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
}
resp=requests.get(url=url,headers=headers)

obj=re.compile(r'<div class="area box">.*?<ul>(?P<adress>.*？)<ul>',re.S)
result=obj.finditer(resp.text)
for it in result:
    adress=it.group('adress')
    print(adress)