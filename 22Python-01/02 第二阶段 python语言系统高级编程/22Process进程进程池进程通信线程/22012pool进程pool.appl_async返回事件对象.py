"""
    pool.apply_async返回事件对象
"""
import multiprocessing
import os
from multiprocessing import Pool
from time import sleep


# 创建进程池事件
def func(msg):
    sleep(2)
    print(os.getpid(),":",msg)
    # 如果需要pool.apply_async返回值,此事件函数就需要返回代码如下
    return msg


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(4)

    # 创建一个存储事件对象返回值列表
    sr = []
    # 添加进程事件
    for i in range(10):
        msg = "Lily%d"%i
        # pool.apply 也可以把事件加入到进程池中,但是一个一个加入,执行完成再执行下一个
        # 而pool.apply_async采用异步方式,同时执行,前提是(进程池中必须要同时执行空闲进程)
        r = pool.apply_async(func=func,args=(msg,))

        # 把pool.apply_async返回值(事件对象)添加到列表中
        sr.append(r)

    # 关闭进程池
    pool.close()
    # 回收进程池
    pool.join()

    # 通过循环返回值事件列表输出各个事件对象
    for i in sr:
        print(i.get())

    # 通过r.get()获取返回事件对象,由于pool.join()已回收进程所以返回是最后一个事件对象
    print(r.get())