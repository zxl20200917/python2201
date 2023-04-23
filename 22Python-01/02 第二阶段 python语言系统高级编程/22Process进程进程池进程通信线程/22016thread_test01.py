"""
    多线程示例
"""
import os
import threading
from time import sleep

a = 1


def func():
    print("开始一个线程", os.getpid())
    sleep(3)
    global a
    print("a = ", a)
    a = 10000
    print("结束线程")


t = threading.Thread(target=func)

t.start()

# 创建主线程
sleep(2)
print("开始一个主线程", os.getpid())


t.join()
print("a = ", a)

# 由于在主线程中a = 10000 ,由此说明主线程与子线程是共用线程进程资源

