import time

from lxml import etree
import requests

url = 'https://www.umeitu.com/bizhitupian/diannaobizhi/'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'}

for i in range(10,100):
    u = 'index_'+str(i)+'.htm'
    url1 = 'https://www.umeitu.com/bizhitupian/diannaobizhi/'+u

    resp = requests.get(url=url1,headers=headers)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    result = html.xpath("/html/body/div[2]/div[8]/ul/li")

    for li in result:
        a=li.xpath('./a/@href')
        b=''.join(a)
        b=b[-10:]
        c = url + b
        child_page = requests.get(c)
        child_page.encoding='utf-8'
        html1 = etree.HTML(child_page.text)
        result1 =''.join(html1.xpath("/html/body/div[2]/div[10]/p/img/@src"))
        img = requests.get(result1)
        img_name = result1[-10:]
        with open("img1/"+img_name,mode="wb") as f:
            f.write(img.content)
            print('over')
            time.sleep(1)
print('all over!')


    #b='https://www.umeitu.com/bizhitupian/'+''.join(a)
    #print(b)'''