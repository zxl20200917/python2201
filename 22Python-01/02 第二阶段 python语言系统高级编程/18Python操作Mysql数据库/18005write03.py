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

# 定义变量给sql传参数第二种方法
name = input("Name:")
age = input("Age:")
sex = input("Sex:")
score = input("Score:")

# 写操作及写数据库
try:
    sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"
    cur.execute(sql,[name,age,sex,score])
    # 操作提交
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
