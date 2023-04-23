"""
        自定义线程类
"""

from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    # 定义线程类,并指定属性
    # 由于target指定线程函数player
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    # 重写run方法
    # 如果不重写run方法,自定义线程对象就会调用线程类原来的run方法
    # 而run方法怎么的指定的player线程函数事件
    # 由于在自定义线程类中定义的target属性,所以target就是指定的player
    def run(self):
        # 如果target代表的是player,而参数由于不确认性,所以需要指定*args **kwargs来指定
        self.target(*self.args, **self.kwargs)


def player(song, sec):
    for i in range(3):
        sleep(sec)
        print("Player %s : %s " % (song, ctime()))


t = MyThread(target=player, args=("葫芦娃", 2))

t.start()
t.join()
