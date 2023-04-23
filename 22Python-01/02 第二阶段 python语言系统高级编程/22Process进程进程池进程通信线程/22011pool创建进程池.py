"""
    创建进程池
"""
import multiprocessing
import os
from multiprocessing import Pool
from time import sleep


# 创建进程池事件
def func(msg):
    sleep(2)
    print(os.getpid(),":",msg)




# windows系统有进程保护,所有无法直接调用各个进程代码,采用两个方法
# 第一种方法: 创建main()函数,调用multiprocessing.freeze_support()
# def main():
#     # 创建进程池
#     pool = Pool(10)
#     # 添加进程事件
#     for i in range(10):
#         msg = "Lily%d"%i
#         pool.apply_async(func=func,args=(msg,))
#
#     # 关闭进程池
#     pool.close()
#     # 回收进程池
#     pool.join()
#
# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#     main()
#

# windows系统有进程保护,所有无法直接调用各个进程代码,采用两个方法
# 第二种方法: 把所有进程代码加入到if __name__ == '__main__': 下执行
if __name__ == '__main__':
    # 创建进程池
    pool = Pool(4)
    # 添加进程事件
    for i in range(10):
        msg = "Lily%d"%i
        pool.apply_async(func=func,args=(msg,))

    # 关闭进程池
    pool.close()
    # 回收进程池
    pool.join()