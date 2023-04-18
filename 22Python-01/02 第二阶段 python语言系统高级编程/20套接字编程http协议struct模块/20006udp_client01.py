"""
    udp客户端编程
"""

from socket import *

# 定义服务端全局变量地址
addr = ('127.0.0.1',8008)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 消息发送
while True:
    msg = input(">>>")
    if not msg:
        break
    sockfd.sendto(msg.encode(),addr)
    data,addr = sockfd.recvfrom(1024)
    print("from server:",data.decode())

sockfd.close()
