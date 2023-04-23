"""
    pool.map
        返回值是函数返回值列表
"""
import multiprocessing
import os
from multiprocessing import Pool
from time import sleep


# 创建进程池事件
def func(n):
    sleep(2)
    print("pool.map执行事件:%d"%n)
    # 如果需要pool.apply_async返回值,此事件函数就需要返回代码如下
    return n*n


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(4)

    # 添加进程事件

    r = pool.map(func=func,iterable=[1,2,3,4,5])


    # 关闭进程池
    pool.close()
    # 回收进程池
    pool.join()


    print(r)
