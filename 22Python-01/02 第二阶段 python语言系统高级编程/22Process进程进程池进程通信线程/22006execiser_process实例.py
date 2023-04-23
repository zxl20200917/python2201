"""
    案例1：拆分文件
    multiprocessing模块完成
    1. 创建两个子进程，同时复制一个文件的上半部分和下半部分，将他们各自复制到一个新的文件里。
    2. 使用os.path.getsize()可以获取文件大小，文件以字节数区分上下半部分
    3. 文件可能是文本文件也可能是二进制文件
"""
import multiprocessing
import os.path
from multiprocessing import Process
import os
from time import sleep

filename = '../20套接字编程http协议struct模块/gg.jpg'
filesize = os.path.getsize(filename)


def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')

    n = filesize//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


def down():
    fr = open(filename,'rb')
    fw = open('down.jpg','wb')
    fr.seek(filesize//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

def main():
    p1 = Process(target=top)
    p1.start()
    p1.join()

    p2 = Process(target=down)
    p2.start()
    p2.join()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()




