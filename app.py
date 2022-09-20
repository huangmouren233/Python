import re

from flask import Flask, session
from flask import render_template
import unit
from flask import request
from flask import jsonify
import xlrd

app = Flask(__name__)


@app.route('/')
def begin_page():
    return render_template("home.html")


@app.route('/index')
def skin():
    return render_template("index.html")


@app.route('/home')
def skin1():
    return render_template("home.html")


@app.route('/wordcloud')
def skin2():
    data = []
    data1=[]
    readexcel = xlrd.open_workbook(r'./allpaper/words.xls', encoding_override='utf-8')
    sheet = readexcel.sheet_by_name('Sheet1')
    for i in range(0, 20):
        # print('第', i + 1, '行数据', sheet.row_values(i), sheet.row_values(i)[0])
        data.append(sheet.row_values(i)[0])
        data1.append(sheet.row_values(i)[1])
    # print(data)
    return render_template("wordcloud.html", data=data, data1=data1)


@app.route('/ICCV2019')
def skin2019():
    data = []
    data1=[]
    readexcel = xlrd.open_workbook(r'./allpaper/words2019.xls', encoding_override='utf-8')
    sheet = readexcel.sheet_by_name('Sheet1')
    for i in range(0, 20):
        # print('第', i + 1, '行数据', sheet.row_values(i), sheet.row_values(i)[0])
        data.append(sheet.row_values(i)[0])
        data1.append(sheet.row_values(i)[1])
    # print(data)
    return render_template("ICCV2019.html", data=data, data1=data1)


@app.route('/compare')
def skin_compare():
    data = []
    data1=[]
    data2=[]
    data3=[]
    readexcel = xlrd.open_workbook(r'./allpaper/words.xls', encoding_override='utf-8')
    readexcel1 = xlrd.open_workbook(r'./allpaper/words2019.xls', encoding_override='utf-8')
    sheet1 = readexcel1.sheet_by_name('Sheet1')
    sheet = readexcel.sheet_by_name('Sheet1')
    for i in range(0, 20):
        # print('第', i + 1, '行数据', sheet.row_values(i), sheet.row_values(i)[0])
        data.append(sheet.row_values(i)[0])
        data1.append(sheet.row_values(i)[1])
        data2.append(sheet1.row_values(i)[0])
        data3.append(sheet1.row_values(i)[1])
    # print(data)
    return render_template("compare.html", data=data, data1=data1, data2=data2, data3=data3)


@app.route('/check', methods=["GET", "POST"])
def checkInfo():
    if request.method == "GET":
        title = request.values.get('title')
        abstract = request.values.get('abstract')
        keywords = request.values.get('keywords')
        sql = '''select * from paper where title like '%%%%%s%%%%' and abstract like '%%%%%s%%%%' and keywords like '%%%%%s%%%%' and href is not null 
        ''' % (title, abstract, keywords)
        print(sql)
        db = unit.MysqlHelper(database='papercarwling', user='root', passwd='15531238359', port=3306, host='localhost')
        data = db.all(sql)
        # print(title)
        # print("122131231231244444")
        # print(data)
        return jsonify({'paper': data})
    else:
        return render_template("index.html", msg="卧槽")


@app.route('/checkall', methods=["GET", "POST"])
def checkall():
    if request.method == "GET":
        sql = 'select * from paper where href is not null'
        db = unit.MysqlHelper(database='papercarwling', user='root', passwd='15531238359', port=3306, host='localhost')
        data = db.all(sql)
        return jsonify({'paper': data})
    else:
        return render_template("index.html", msg="卧槽")


@app.route('/delete')
def delete():
    if request.method == "GET":
        title = request.values.get('title')
        sql = 'delete from paper where title = "%s"' % (title)
        print(sql)
        db = unit.MysqlHelper(database='papercarwling', user='root', passwd='15531238359', port=3306, host='localhost')
        msg = db.cud(sql)
        print(msg)
        return render_template("index.html")
    else:
        return render_template("index.html", msg="卧槽")

# def wordcloud():


#登录
@app.route('/login', methods=['GET', "POST"])
def login():
    user = str(request.args.get('account'))
    pwd = str(request.args.get('password'))
    print(user)
    if not user:
        return jsonify({'data': 2})
    elif not re.match("^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$",user):
        return jsonify({'data': 3})
    if not pwd:
        return jsonify({'data': 4})
    db = unit.MysqlHelper(database='papercarwling', user='root', passwd='15531238359', port=3306, host='localhost')
    res = db.psdright(user, pwd)
    if res == 1:
        return jsonify({'data': 1})
    else:
        return jsonify({'data': 2})


#注册
@app.route('/register', methods=['GET', "POST"])
def register():
    user = request.args.get('account')
    pwd = request.args.get('password')
    name = request.args.get('name')
    if not name:
        return jsonify({'data': 5})
    if not user:
        return jsonify({'data': 2})
    elif not re.match("^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$",user):
        return jsonify({'data': 3})
    if not pwd:
        return jsonify({'data': 4})
    db = unit.MysqlHelper(database='papercarwling', user='root', passwd='15531238359', port=3306, host='localhost')
    state = db.insert(user, pwd, name)
    if state == 1:
        return jsonify({'data': 1})
    else:
        return jsonify({'data': 6})


#前往注册|登录页面
@app.route('/log')
def loginhtml():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()

# from flask import Flask
# from flask import render_template
# from flask_bootstrap import Bootstrap
# import pymysql
# app = Flask(__name__)
# bootstrap = Bootstrap(app)
#
#
# @app.route('/')
# def index():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='15531238359', db='papercarwling', charset='utf8')
#     cur = conn.cursor()
#     sql = "SELECT * FROM paper"
#     cur.execute(sql)
#     u = cur.fetchall()
#     conn.close()
#     return render_template('index.html', u=u)
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
