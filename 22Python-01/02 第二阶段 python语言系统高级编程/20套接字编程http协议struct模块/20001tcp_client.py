"""
    tcp客户端连接
"""
from socket import *

# 依据默认值，创建套接字
sockfd = socket()  # 默认值

# 创建服务端地址
server_addr = ('127.0.0.1',8888)

# 发起连接
sockfd.connect(server_addr)

# 收发消息
while True:
    msg = input(">>")
    sockfd.send(msg.encode())
    if msg == "##":
        break
    data = sockfd.recv(1024)
    print("from server:", data.decode())

# 关闭套接字
sockfd.close()
