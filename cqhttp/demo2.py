import requests


def keywor(message, uid, gid=None):
    if message == '来张图':
        setu(uid, gid)


def setu(uid, gid=None):
    num = 20
    url = 'https://api.lolicon.app/setu'
    params = {'r18': 1,
              'size1200': True,
              'num': num}
    menu = requests.get(url, params=params)
    # print(menu.json()['data'][0]['urls']['original'])
    for i in range(num):
        print(menu.json()['data'][i]['url'])
        setu_url = menu.json()['data'][i]['url']  # 对传回来的网址进行数据提取

        if gid:
            put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
            pic_path = r'[CQ:image,' r'file=' + setu_url + r']'
            print(pic_path)
            requests.get(url=put.format(gid, pic_path))
            requests.get(url=put.format(gid, '已经发了一张图，没看到就是被吞了'))
        else:
            print(uid)
            put = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
            pic_path = r'[CQ:image,' r'file=' + setu_url + r']'
            print(pic_path)
            requests.get(url=put.format(uid, pic_path))
