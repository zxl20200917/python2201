"""
    mysql写操作
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

# 写操作及写数据库
try:
    sql = "insert into cls values (5,'tty02',31,'m',92.8);"
    cur.execute(sql)
    sql = "update cls set score=77.5 where id=1;"
    cur.execute(sql)
    sql = "delete from cls where id = 3;"
    cur.execute(sql)
    # 操作提交
    db.commit()
except Exception as e:
    db.rollback()



# 关闭游标和数据库
cur.close()
db.close()
