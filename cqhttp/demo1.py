from flask import Flask, request
import requests
app = Flask(__name__)


@app.route('/', methods=["POST"])
def post():
    if request.get_json().get('message_type') == 'private':  # 私聊信息
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        keyword(message, uid)  # 将 Q号和原始信息传到我们的后台

    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
def keyword(message, uid, gid=None):
    if message == '来张图':
        setu(uid,gid)

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
            put = 'http://127.0.0.1:6700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
            pic_path = r'[CQ:image,' r'file=' + setu_url + r']'
            print(pic_path)
            requests.get(url=put.format(gid, pic_path))
            requests.get(url=put.format(gid, '已经发了一张图，没看到就是被吞了'))
        else:
            print(uid)
            put = 'http://127.0.0.1:6700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
            pic_path = r'[CQ:image,' r'file=' + setu_url + r']'
            print(pic_path)
            requests.get(url=put.format(uid, pic_path))
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)  # 此处的 host和 port对应上面 yml文件的设置