import traceback

import pymysql


class MysqlHelper():
    def __init__(self, host, port, database, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = database
        self.user = user
        self.password = passwd
        self.charset = charset

    def open(self):
        # 连接数据库
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db,
                                    user=self.user, passwd=self.password, charset=self.charset)
        # 创建游标对象
        self.cursor = self.conn.cursor()

    # 关闭
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 增加、修改、删除命令语句
    def cud(self, sql, params=(), msg="操作成功！"):
        try:
            self.open()
            # 处理逻辑数据，传入sql语句以及参数化
            self.cursor.execute(sql, params)
            # 执行事务
            self.conn.commit()
            self.close()
            # 这样可以修改输出的操作成功信息提示
            print(msg)
            return msg
        except Exception as e:
            self.conn.rollback()
            print("错误", e)
            return e

    # 查询所有数据,多个值
    def all(self, sql, params=()):
        try:
            self.open()
            self.cursor.execute(sql, params)
            data = self.cursor.fetchall()
            self.close()
            return data
        except Exception as e:
            print("错误", e)

    def psdright(self, username, password):
        sql = 'select * from user1 where username = ' + username + ' and password = ' + password
        try:
            res = self.all(sql)
            if res and password == res[0][2]:
                return 1
            elif res and password != res[0][2]:
                return 2
        except:
            return 3

    def insert(self, a, p, n):
        self.open()
        try:
            state = 1
            # sql = 'insert into users(account,password,telephone,travel,physical,education,fashion,technology,entertainment,history,pets,health,finance,username) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            SQL = 'insert into user(username,password,name1) values(%s,%s,%s)'
            # info = [str(a), str(p), str(t), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', str(name)]
            info = [a, p, n]
            self.cursor.execute(SQL, info)
            self.conn.commit()
        except:
            state = 2
            traceback.print_exc()
        finally:
            self.close()
        return state


if __name__ == '__main__':
    db = MysqlHelper(database='zzsfp', user='root', passwd='000000', port=3306, host='192.168.2.128')

    sql = 'select * from last '
    data = all(sql)
    print(data)
