"""
    发送端：send为客户端
"""

from socket import socket

s = socket()
s.connect(('127.0.0.1', 8001))

# 读取目标文件，循环发送
f = open('../18Python操作Mysql数据库/1.jpg', 'rb')
while True:
    # 边读取，边发送
    data = f.read(1024)
    if not data:
        break
    s.send(data)

# 关闭连接对象及文件对象
s.close()
f.close()
