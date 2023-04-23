"""
    process创建带参数的子进程绑定函数
    args 元组 与 kwargs是字典传参 混合用传参

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
    # args 与kwargs两个混用
    # args=(2,) 就算只有一个参数，也要用逗号分开，保证是一个元组
    p = Process(target=worker, args=(2,),kwargs={'name':'Jeck'})
    p.start()
    p.join()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
