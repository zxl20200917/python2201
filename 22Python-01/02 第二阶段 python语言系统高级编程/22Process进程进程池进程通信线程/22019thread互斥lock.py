"""
    lock 实例
    lock加锁与解锁要应用在所有关联的代码部分
"""

from threading import Thread,Lock
from time import sleep


# 定义Lock对象
lock = Lock()
a = b = 0


def value():
    while True:
        lock.acquire()      # 上锁
        if a != b:
            print("a = %d,b = %d" % (a, b))

        lock.release()      # 解锁


t = Thread(target=value)
t.start()

# 定义父线程函数
while True:
    with lock:          # 上锁
        a += 1
        sleep(1)
        b += 1
                        # with代码块结束自动解锁


t.joint()
