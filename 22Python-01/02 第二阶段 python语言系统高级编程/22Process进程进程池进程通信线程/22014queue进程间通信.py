"""
    消息队列
"""

from multiprocessing import Process
from multiprocessing import Queue
from time import sleep

# FIFO
q = Queue(3)


def bar(queue):
    for i in range(4):
        sleep(2)
        msg = "第%d次增加队列于队列为:%d"%(i,i )
        queue.put(msg)


def foo(queue):
    while True:
        try:
            print(queue.get(timeout=3))
        except:
            return

def main():
    p1 = Process(target=bar,args=(q,))
    p2 = Process(target=foo,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()