"""
    mysql读操作
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

# 对数据读操作
sql = "select * from cls;"
cur.execute(sql)  #数据库读操作，通过此游标返回是可迭代对象，所以只能通过可迭代对象进行读出

# # 读操作第一种方法，通过迭代对象读取数据
# for i in cur:
#     print(i)

# 读操作第二种方法，通过函数cur.fetchone()
#one = cur.fetchone()
#print(one)


# 读操作第三种方法，通过函数cur.fetchmany
# many = cur.fetchmany(2)
# print(many)

# 读操作第三种方法，通过函数cur.fetchall
all = cur.fetchall()
print(all)


# 关闭游标和数据库
cur.close()
db.close()
