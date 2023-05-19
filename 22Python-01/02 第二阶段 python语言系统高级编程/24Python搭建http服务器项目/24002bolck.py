# coding:utf-8
# @Author:CC

"""
    非阻塞IO
"""

from socket import *
from time import sleep


s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

# s.setblocking(False)
# 设置套接字超时时间
s.settimeout(3)


while True:
    print("waiting for connect....")
    try:
        c,addr = s.accept()
    except BlockingIOError as e:
        print(e)
        sleep(2)
    else:
        print("connect from:",addr)
        data = c.recv(1024)
