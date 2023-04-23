"""
    名称: FTP server 文件服务器服务端
    env: python3.11
    模型: TCP 多线程并发
"""
import wsgiref.validate
from socket import *
from threading import *
import sys, os
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
# ftp 文件库(用本地一个目录作为ftp文件库)
FTP = "E:\\develop\\test\\"


# 客户端处理类 查看服务器 上传  下载
class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self):
        # 获取文件列表
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            # 为防止‘OK'与下面files文件代码粘连，所以用时间进行间隔一下
            sleep(0.01)

        # 发送文件
        # files = ""
        # for file in file_list:
        #     files += file + '\n'
        # 上面注释代码可以替换来如下：为回车'\n'来拼接每个文件
        files = '\n'.join(file_list)
        self.connfd.send(files.encode())

    def do_get(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception as e:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            # 加时间时隔就是为防止TCP粘包问题
            sleep(0.01)

        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                # 加时间时隔就是为防止TCP粘包问题
                sleep(0.01)
                # if not data 表示文件为空时，就是文件结尾了，所以发送'##'，并跳出循环发送
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()

    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')

        # 接收文件
        f = open(FTP + filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    def run(self) -> None:
        # 接收客户端请求
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)

# 搭建网络模型
def main():
    # 创建TCP套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    print("Listen the port 8888")
    # 循环等待客户端链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from addr:", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务端退出...")
        except Exception as e:
            print(e)
            continue

        t = FTPServer(c)
        t.start()


if __name__ == '__main__':
    main()
