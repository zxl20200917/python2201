"""
    查找单词
    客户端
"""

from socket import *
# 服务器地址
ADDR = ('127.0.0.1',8009)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("word>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print(msg.decode())

sockfd.close()