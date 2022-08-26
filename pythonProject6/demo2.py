import requests
import re

proxy_support = requests

#获取URL的html
def Get_html(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    r = requests.get(url,headers = header) #用Get方法并改变headers
    r.encoding = r.apparent_encoding
    return r.text

#获取图片相对应的URL
def Get_Image_url(html):
    Image_urls = re.compile('http://i1.whymtj.com/uploads/tu/201903/9999/.*?\.jpg').findall(html) # 用正则表达式从HTML中获取图片的URL
    return Image_urls

# 从每个图片对应的URL中获取信息，并保存在文件夹里
def Save_Image(Image_url):
    r = requests.get(Image_url)
    root = 'C:\\Users\\lijun' # 保存图片的路径
    path = root + Image_url.split('/')[-1] # Image_url.split('/')[-1]为文件的名字
    with open (path,'wb') as f:
        f.write(r.content)
        f.close()

# 主函数
def main():
    #爬取三页的图片
    count = 3
    while count >= 1:
        url = 'http://www.umei.cc/weimeitupian/' + str(count) + '.htm'
        html = Get_html(url)
        Image_urls = Get_Image_url(html)
        for Image_url in Image_urls:
            Save_Image(Image_url)
        count -= 1


if __name__ == '__main__':
    main()