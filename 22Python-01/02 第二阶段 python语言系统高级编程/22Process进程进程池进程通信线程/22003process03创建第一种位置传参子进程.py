"""
    process创建带参数的子进程绑定函数
    args传参的方式是通过位置进行传参数的

"""
import multiprocessing
from multiprocessing import Process
from time import sleep

# 创建带有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working.....")


def main():
    # args位置传参是一个元组
    p = Process(target=worker,args=(2,'tom'))
    p.start()
    p.join()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
