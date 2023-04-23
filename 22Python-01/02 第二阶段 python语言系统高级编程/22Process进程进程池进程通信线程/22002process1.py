"""
    process简单进程创建
    在全局设置一个变量a赋值为1，在子进程里修改为10000，然后打印分别打印父子进程调用的变量值
    如果父子进程调用变量为发生变化都为10000，那就说明父子进程是执行同样内存空间。
    如果父子进程调用变量只发生子进程，而父进程还是原来全局变量值，就说明父子进程是分别执行的，而执行的内存
    空间也是不同的。
"""
import multiprocessing
import multiprocessing as mp
from time import sleep

# 定义全局变量a
a = 1


# 进程执行函数
def func():
    print("开始一个进程")
    global a
    a = 10000
    print("子进程变量a=", a)
    sleep(3)
    print("进程结束")


# 创建进程对象
p = mp.Process(target=func)


# # 启动进程
# p.start()
#
# # 回收进程
# p.join()

def main():
    p.start()
    sleep(2)
    print("父进程执行内容")
    print("父进程变量a=", a)
    p.join()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
