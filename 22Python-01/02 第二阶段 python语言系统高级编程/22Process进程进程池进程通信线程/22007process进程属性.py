"""
    进程对象属性
"""
import multiprocessing
from multiprocessing import Process
from time import sleep


def func():
    print("进程对象属性测试")
    sleep(3)
    print("进程结束")


def main():
    # 不指定子进程名称，默认为process-1,
    # 通过name指定子进程名称，方便进行进程管理
    p = Process(target=func,name="test01")
    # deamon在此并不传统意义上的子进程的守护进程的，默认False，说明主进程退出不影响子进程
    # 设置True话的，主进程退出会让的所有子进程退出，设置需要在start()之前
    p.daemon = True
    p.start()
    print("PID: ",p.pid)
    print("name:",p.name)
    print("daemon:",p.daemon)
    # 如果增加如下代码，说明主进程阻塞，等待子进程执行，如果把join()代码注释的话，主进程执行完上面三行代码
    # 就退出了，由于daemon设置为true，所以就不会执行子进程了。
    p.join()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

