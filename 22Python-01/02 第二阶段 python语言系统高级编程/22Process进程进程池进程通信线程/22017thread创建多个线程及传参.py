"""
    创建多个线程及传参
"""

from threading import Thread
from time import sleep


def music(sec,name):
    sleep(sec)
    print("播放%s"%name)

# 创建多线程列表
l = ['黄河大合唱','国际歌','中国心']


# 创建线程列表
jobs = []

# 采用循环方式进行创建多个线程
for i in l:
    t = Thread(target=music,args=(2,i))
    jobs.append(t)
    t.start()

# 回收多个线程
for i in jobs:
    i.join()


