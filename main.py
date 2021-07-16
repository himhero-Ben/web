from flask import Flask, render_template, request, redirect
import urllib.request
import time
import ssl
import json
import string


def say():
    while True:

        # def talk():
        target = r'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        keyword = '校园笑话'
        if keyword == "exit":
            print("不聊算了，拜拜")
            break
        tmp = target + keyword
        url = urllib.parse.quote(tmp, safe=string.printable)
        page = urllib.request.urlopen(url)
        html = page.read().decode("utf-8")
        res = json.loads(html)
        return res['content'].replace('{br}', '').replace('提示：按分类看笑话请发送“笑话分类”', '').replace('(校园)', ' :')


# 创建程序
# web应用程序
app = Flask(__name__)


def op(user, password):
    with open('txxt.txt', 'a') as f:
        f.write(user)
        f.write(',')
        f.write(password)
        f.write(';')


@app.route('/welcome', methods=['POST', 'GET'])
def index():
    return render_template("hhh.html")


@app.route('/', methods=['POST', 'GET'])
def index2():
    return render_template("hh.html", no=' ')


@app.route('/Start_Here', methods=['POST', 'GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('pw')
    a = []
    # try:
    with open('txxt.txt', 'r') as l:
        m = l.read()
        s = m.split(';')
        for k in s:
            if k == '':
                g = s.pop(s.index(k))
            a.append(k.split(','))
        b = []
        n = []
        for q in a:
            if q == ['']:
                a.remove([''])
        for u, p in a:
            b.append(u)
            n.append(p)
        if (username and password == '') or (len(username) + len(username) <= 8):
            print(f'内部没有{username} {password}的用户')
            return render_template('hh.html', no='账号不为空或长度不够')
        elif (username in b) and (password in n):
            print(username,'已上线')
            return render_template('h.html', name=username, txt=say())
        elif username not in b:
            op(username, password)
            print(username,password,'成功注册')
            return '<font color="red">注册成功!</font>'
    # except:
    #     return '???'


app.run(host='0.0.0.0', port=49677)
