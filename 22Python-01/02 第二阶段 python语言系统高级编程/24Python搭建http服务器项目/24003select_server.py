"""
    基于select的socket复用
"""

from select import select
from socket import *


HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 创建套接字，作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

# 初始select关注监听套接字
rlist = [s]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    for r in rs:
        if r is s:
            # 处理客户端的链接
            c, addr = r.accept()
            # 把连接客户端存放到列表中
            rlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            r.send(b'OK')





