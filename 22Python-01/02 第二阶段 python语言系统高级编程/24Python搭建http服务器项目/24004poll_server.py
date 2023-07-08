"""
    基于poll方法的socket服务
"""


from select import select,poll,POLLIN
from socket import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 创建套接字，作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)


s.setblocking(False)

# 生成poll对象
p = poll()

# 关注套接字
p.register(s,POLLIN)

# 建立字典，特点：时刻与关注的IO保持一致
fdmap = {s.fileno():s}

# 循环监控IO发生
while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            c.setblocking(False)
            p.register(c,POLLIN)
            fdmap[c.fileno()] = c
        else:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                continue
                print(data)
                fdmap[fd].send(b'OK')

