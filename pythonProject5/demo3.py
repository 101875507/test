import  requests
'''q= input('请输入要搜索的内容：')
url = f'https://cn.bing.com/search?q={q}'
/537.36 Edg/98.0.1108.62'}headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari
resp = requests.get(url,headers=headers)
print(resp)
print(resp.text)'''
'''url = 'https://fanyi.baidu.com/sug'
requests.post(url)
s = input('请输入你要翻译的单词：')
data = {'kw':s}
resp = requests.post(url,data=data)
print(resp.json())'''
'''url = 'https://movie.douban.com/j/chart/top_list'
dict = {'typ': '24',
'interval_id': '100:90',
'action':'',
'start': '0',
'limit': '20'}
/537.36 Edg/98.0.1108.62'}headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari
r=requests.get(url=url,params=dict,headers=headers)
print(r.request.url)
print(r.text)
r.close()'''
'''lst1 = [1,2,3,4,5,6]
lst2 = [2,3,4,5,6,7]
lst3 =[]
for i in range(0,6):
    b = lst1[i]*lst2[i]
    lst3.append(b)
    i=i+1
print(lst3)'''
from string import digits
from random import choice
z = ''.join(choice(digits) for i in range(100000000))
result = {}
for ch in z:
    result[ch] = result.get(ch,0) + 1
for digits, fre in sorted(result.items()):
    print(digits,fre,sep=':')




