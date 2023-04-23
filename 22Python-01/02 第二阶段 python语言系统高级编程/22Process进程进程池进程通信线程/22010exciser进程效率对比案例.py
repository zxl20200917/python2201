"""
    进程效率对比
        分别求证使用4个进程和10个进程计算100000以内质数之和的时间，与单进程时间比较，看是否提高运行效率
"""

import multiprocessing
import time


# 定义时间装饰器
def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.8f" % (f.__name__, end_time - start_time))
        return res

    return wrapper


def ifprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True


# 首先单个子进程的计算时间
@timeit
def no_mutil_process():
    prime = []
    for i in range(1, 100001):
        if ifprime(i):
            prime.append(i)
    sum(prime)


# 自定义进程类，并创建prime质数列表，开始节点，结束节点
class prime2(multiprocessing.Process):
    def __init__(self, prime, begin, end):
        super().__init__()
        self.prime = prime
        self.begin = begin
        self.end = end

    # 重写run方法，从开始节点至结束节点进行判断是否为质数
    def run(self):
        for i in range(self.begin, self.end):
            if ifprime(i):
                self.prime.append(i)

        sum(self.prime)


# 创建4个子进程函数
@timeit
def use_multi_process():
    prime = []
    process = []
    for i in range(1, 100001, 25000):
        p = prime2(prime, i, i + 25000)
        p.start()
        process.append(p)

    for i in process:
        i.join()


@timeit
def use10_multi_process():
    prime = []
    process = []
    for i in range(1, 100001, 10000):
        p = prime2(prime, i, i + 10000)
        p.start()
        process.append(p)
    for i in process:
        i.join()


def main():
    # no_mutil_process()      # no_mutil_process函数运行时间：25.81730723
    # use_multi_process()       # use_multi_process函数运行时间：12.87275863
    use10_multi_process()       #use10_multi_process函数运行时间：9.70128775


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
