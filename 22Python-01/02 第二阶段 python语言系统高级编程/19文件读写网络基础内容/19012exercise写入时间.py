"""
    写入时间
    1. 每隔2秒向文件写入一个当前时间，格式为：
        1. 2023-05-05 10:10:12
        2. 2023-05-05 10:10:14
        3. 2023-05-05 10:10:16
    当程序结束重写启动时，继续写入时间，并且序号能够衔接
"""
import time

f = open("log.txt", 'a+')

# a打开文件偏移在结尾，移动到开头
f.seek(0,0)
n = 0

# 获取现有文件有多少行
for line in f:
    n += 1

while True:
    n += 1
    time.sleep(2)
    s = "%d. %s\n" % (n, time.ctime())
    f.write(s)
    f.flush()

