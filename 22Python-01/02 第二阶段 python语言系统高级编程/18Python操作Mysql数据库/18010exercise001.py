"""
    编写一个类完成注册和登录
        编写一个类，实例化对象时可以连接数据库，通过该对象调用方法可以模拟完成简单的登录注册功能。
"""

import pymysql


class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(
            host='192.168.42.237',
            port=3306,
            user='root',
            password='zhangxuelong',
            database='stu',
            charset='utf8'
        )

        # 生成游标对象(操作数据库，执行sql语句，获取结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    def register(self, name, password):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False
        else:
            sql = "insert into user (name,password) values (%s,%s);"
            try:
                self.cur.execute(sql, [name, password])
                self.db.commit()
                return True
            except Exception as e:
                print(e)
                self.db.rollback()
                return False

    def login(self, name, password):
        # 数据库查找
        sql = "select * from user where name='%s' and passwd='%s';" % (name, password)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False


if __name__ == '__main__':
    db = Database()
    db.register('Tom', '123')
    db.login('Tom', '123')
    db.close()
