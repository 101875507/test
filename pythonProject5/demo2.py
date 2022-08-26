'''from urllib3 import *
from re import *
http = PoolManager()
disable_warnings()
def downlaoad(url):
    result = http.request('GET',url)
    htmlStr = result.data.decode('utf-8')
    return htmlStr
def analyse(htmlStr):
    alist = findall('<a[^>]*titleink[^>]*>[^<]*</a>',htmlStr)
    result = []
    for a in alist :
        g = search('href[\s]*=[\s]*[\'"]([^\'""]*)[\'"]',a)
        if g != None :
            url =g.group(1)
        index1 = a.find(">")
        index2 = a.find("<")
        title = [index1+1,index2]
        d ={}
        d['url']=url
        d['title']=title
        result.append(d)
    return result
def crawler(url) :
    html =downlaoad(url)
    bloglist = analyse(html)
    for blog in bloglist :
        print("title:",blog['title'])

crawler('https://www.cnblogs.com/')'''
import requests

url = 'http://www.baidu.com/'
url1 = 'https://www.csdn.net/'

response = requests.get(url)
response1 = requests.get(url1)

print(response)#返回结果为418，200为请求成功，418则是对方发现咱们是爬虫了
print(response1)'''



