"""
    mysql写操作-存储二进制图片
    首先在数据库中增加一个字段img
        alter table cls add img blob;
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

# 对图片进行二进制方式存储写操作
# sql = "update cls set img=%s where id = 1;"
# f = open('zxl.jpg','rb')
# data = f.read()
#
# try:
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()

# 对图片进行二进制方式读操作
sql = "select img from cls where id = 1;"
cur.execute(sql)
# cur.fetchone返回值是一个元组的第一个元组数据，所以data[0]
data = cur.fetchone()
# cur.fetchone返回值是一个元组的第一个元组数据，所以data[0]
with open('1.jpg','wb') as f:
    f.write(data[0])

# 关闭游标和数据库
cur.close()
db.close()
