import requests
'''session = requests.session()
data = {
'loginName': "1018875507li",
'password': "a12345678"
}
url = 'https://passport.17k.com/ck/user/login'
session.post(url=url,data=data)'''
#print(resp.cookies)
'''resp = requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919',headers={'Cookie': 'GUID=ddeb9ca9-0533-456a-b408-32592f221b53; BAIDU_SSP_lcr=https://www.baidu.com/link?url=wq1OyXq8Us1l3SAduq-wctO17D947yYAfY94J67Y4m_&wd=&eqid=ff5f77c8001aa83b000000026236dada; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1647762146; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F17%252F17%252F11%252F94291117.jpg-88x88%253Fv%253D1647761167000%26id%3D94291117%26nickname%3D1018875507li%26e%3D1663314192%26s%3D8d585ed26675aa50; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2294291117%22%2C%22%24device_id%22%3A%2217fa647024f1be-0a1f2469624fa6-3e604809-1327104-17fa647025013a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22ddeb9ca9-0533-456a-b408-32592f221b53%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1647763054'})
print(resp.text)'''





url = 'https://www.pearvideo.com/video_1755627'
contid = url.split("_")[1]
print(contid)
url1 = f'https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.3868237932928793'
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
           'Referer': 'https://www.pearvideo.com/video_1755627'}

resp = requests.get(url1,headers=headers)
dic = resp.json()
systemTime = dic['systemTime']
srcurl = dic['videoInfo']["videos"]["srcUrl"]
srcurl = srcurl.replace(systemTime,f'cont-{contid}')
print(srcurl)
with open('a.mp4',mode='wb') as f:
    f.write(requests.get(srcurl).content)



