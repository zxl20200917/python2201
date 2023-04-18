"""
    chat root 客户端

"""

from socket import *
import os, sys

# 服务端地址
ADDR = ('127.0.0.1', 8888)

# 创建发送消息函数send_msg()
def send_msg(s,name):
    while True:
        text = input("发言:")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)


# 创建接收消息函数recv_msg()
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(4096)
        print(data.decode())
# 搭建网络
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    # 进入聊天室
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        # 得到服务端反馈
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("进入聊天室")
            break
        else:
            print(data.decode())

    # 创建进程（两个进程一个子进程一个父进程，子进程发送消息，父进程接收消息）
    pid = os.fork()
    if pid < 0:
        print("Error")
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)



if __name__ == '__main__':
    main()
