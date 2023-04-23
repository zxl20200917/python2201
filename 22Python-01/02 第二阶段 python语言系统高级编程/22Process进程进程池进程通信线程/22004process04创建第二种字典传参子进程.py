"""
    process创建带参数的子进程绑定函数
    kwargs是字典传参，是基于键的名称进行传参的

"""
import multiprocessing
from multiprocessing import Process
from time import sleep


# 创建带有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working.....")


def main():
    # kwargs是一个字典，是基于键的名称进行传参
    p = Process(target=worker, kwargs={'name':'Lily','sec':2})
    p.start()
    p.join()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
