"""
    mysql 写操作通过input输入
"""

import pymysql

# 链接数据库
db = pymysql.connect(
    host='192.168.42.237',
    port=3306,
    user='root',
    password='zhangxuelong',
    database='stu',
    charset='utf8'
)

# 生成游标(游标对象用于执行sql语句，获取执行结果)
cur = db.cursor()

# 定义变量给sql传参数第一种方法
name = input("Name:")
age = input("Age:")
sex = input("Sex:")
score = input("Score:")

# 写操作及写数据库
try:
    sql = "insert into cls (name,age,sex,score) values ('%s',%s,'%s',%s);" % (name, age, sex, score)
    # '%s' 表示一定要符合mysql定义字段，由于name,sex为字符所以要用''引号给括起来，不然为生成sql是不带引号，就无法在mysql中无法执行。
    cur.execute(sql)
    # 操作提交
    db.commit()
except Exception as e:
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
