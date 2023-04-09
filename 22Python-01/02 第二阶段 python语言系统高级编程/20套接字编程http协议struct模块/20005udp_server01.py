"""
    udp服务
"""

from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8008))

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    if not data:
        break
    print("connect from %s:%s" % (addr, data.decode()))
    sockfd.sendto(b'ok', addr)

sockfd.close()
