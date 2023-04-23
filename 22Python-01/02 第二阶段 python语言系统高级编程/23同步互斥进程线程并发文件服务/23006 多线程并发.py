"""
     多线程并发
"""

from socket import *
from threading import Thread

# 定义全局变量
ADDR = ('0.0.0.0', 8888)


# 客户端处理函数
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")

# 循环等待客户端连接
while True:
    # 对服务端要处理异常
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        s.close()
        exit()
    except Exception as e:
        print(e)
        continue

    t = Thread(target=handle, args=(c,))
    t.daemon = True
    t.start()
