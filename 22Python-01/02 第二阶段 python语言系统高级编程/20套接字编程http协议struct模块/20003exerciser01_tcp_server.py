"""
    服务端为接收端：recv
"""
from socket import socket
s = socket()
s.bind(('127.0.0.1',8001))
s.listen(3)

conn,addr = s.accept()
print("connect from ",addr)

# 接收思路：
#   1. wb写打开文件
#   2. recv 内容 write文件

# 打开文件
f = open('gg.jpg','wb')

# 循环接收写入文件
while True:
    data = conn.recv(1024)
    # not data 作为判断的依据是等待客户端发过来空，自动跳出，但是客户是发送完文件是不能发过来一个空的
    # 解决方法原因：是由于客户在发送完文件时，会触发s.close,这样另一端的recv就会返回一个空
    # 这个not data 判断依据是来自这里。
    if not data:
        break
    f.write(data)

f.close()
s.close()
conn.close()