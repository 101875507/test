from flask import Flask, request

'''注意，这里的import api是另一个py文件，下文会提及'''


app = Flask(__name__)

'''监听端口，获取QQ信息'''


@app.route('/', methods=["POST"])
def post_data():
    #print(request.get_json())
    if request.get_json().get('message_type') == 'private':
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        print(uid)
        print(message)
    return 'OK'




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)  # 此处的 host和 port对应上面 yml文件的设置

