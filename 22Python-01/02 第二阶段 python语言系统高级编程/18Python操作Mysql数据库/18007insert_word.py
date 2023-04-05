"""
    在dict数据库中建立words表存储单词。将dict.txt文件中单词写入到words数据表中
"""

import pymysql

# 链接数据库
db = pymysql.connect(
    host='192.168.42.237',
    port=3306,
    user='root',
    password='zhangxuelong',
    database='dict',
    charset='utf8'
)

# 生成游标(游标对象用于执行sql语句，获取执行结果)
cur = db.cursor()

f = open('dict.txt')
# 插入单词
args_list = []
for line in f:
    # 获取单词和解释
    # split依据空格切割，切割一项
    word,mean = line.split(' ',1)
    # 由于切割出来mean前面后面都有空格，所以需要通过mean.strip()把两边空格去除
    args_list.append((word,mean.strip()))

# 写操作及写数据库
try:
    sql = "insert into words (word,mean)values (%s,%s); "
    cur.executemany(sql,args_list)
    # 操作提交
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
