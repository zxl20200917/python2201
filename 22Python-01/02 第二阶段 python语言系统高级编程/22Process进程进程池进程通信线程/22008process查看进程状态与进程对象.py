"""
    查看进程状与获取进程对象
"""
import multiprocessing
import multiprocessing as mp
from multiprocessing import Process
from time import sleep


def func():
    print("进程对象属性测试")
    print("进程对象：", mp.current_process)
    # 可以基于进程对象，进行进程属性的查看,如下：
    print(mp.current_process().name)
    print(mp.current_process().pid)
    print(mp.current_process().daemon)
    sleep(3)
    print("进程结束")


def main():
    p = Process(target=func,name="p01")
    p.start()
    print("进程状态：",p.is_alive())
    p.join()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

