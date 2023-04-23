"""
    fork多进程并发server
"""

from socket import *
import os

# 定义全局变量
ADDR = ('0.0.0.0', 8888)


# 客户端处理函数
def handle():
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

    # 创建子进程处理连接进来的客户端
    pid = os.fork()
    if pid == 0:
        # 而对于子进程是处理客户端的连接,所以s.close
        s.close()
        # 子进程处理客户端请求需要封装到一个函数中
        handle()
    else:
        # 包括了pid<0与pid>的情况,这两情况都是为让他进一步循环等待客户端连接
        # 由于父进程循环处理的 就是客户端连接,所以对c.close就没有用了
        c.close()
