"""
    同步互斥Event操作实例
        e = thread.Event
        e.wait()
            wait阻塞状态依据Eventg事件状态设置是否,如果设置e.set()则阻塞,末设置e.clear()则不阻塞
"""

from threading import Thread,Event
from time import sleep

e = Event()
# 定义一个全局变量
a = 100

# 定义一个线程函数事件
def func():
    global a
    a = 1
    print("运行子线程")
    print("打印子线程全局变量a=",a)
    e.set()


t = Thread(target=func)
t.start()
# 开启主线程
e.wait()
if a != 1:
    print("主线程调用a的变量值为:",a)
else:
    print("主线程与子线程共享全局变量a=",a)

t.join()
