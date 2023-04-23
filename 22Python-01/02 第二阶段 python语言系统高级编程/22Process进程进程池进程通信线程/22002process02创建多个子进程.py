"""
    proccess 一次性创建多个子进程的方法
    在process过程中创建的进程，一般不会要求主进程处理过多事务，它的主要作用就是创建子进程
    而具体工作内容由多个子进程来执行的
"""
import multiprocessing
from multiprocessing import Process
import os
from time import sleep


# 创建三个子进程绑定的功能函数
def func1():
    sleep(3)
    print(os.getppid(), '---', os.getpid(), '吃饭')


def func2():
    sleep(2)
    print(os.getppid(), '---', os.getpid(), '睡觉')


def func3():
    sleep(4)
    print(os.getppid(), '---', os.getpid(), '打豆豆')


# 定义一个全局工作列表，把多个子进程全局放入列表中
jobs = []


# 定义一个循环启动的函数来分别启动多个子进程
def UpProcess():
    for i in [func1, func2, func3]:
        p = Process(target=i)
        jobs.append(p)
        p.start()


# 定义一个循环关闭多个子进程
def DownProcess():
    for i in jobs:
        i.join()


def main():
    UpProcess()
    DownProcess()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
