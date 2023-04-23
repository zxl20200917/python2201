"""
    FTPclient
"""
import time
from socket import *
import sys, os

# 服务地址
ADDR = ('127.0.0.1', 8888)


# 具体请求功能
class FTPCliet():
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        # 向服务端发送请求
        self.sockfd.send(b'L')
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(1024*1024)
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(("G "+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 首先打开一个本地文件,文件名就是传过来的文件名称
            f = open(filename,'wb')
            # 循环接收文件
            while True:
                data = self.sockfd.recv(1024)
                # 判断文件结尾,如果服务端发送过来是'##'就是文件结束标志
                if data == b'##':
                    break
                f.write(data)
            f.close()

        else:
            print(data)

    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except Exception:
            print("该文件不存在")
            return
        # 获取文件名
        filename = filename.split('/')[-1]
        # 发送请求
        self.sockfd.send(('P '+ filename).encode())
        # 接收反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)




# 搭建网络
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return
    # 实例化对象
    ftp = FTPCliet(s)

    # 循环发送请求
    while True:
        print("\n================Command================")
        print("================  list ================")
        print("================get file================")
        print("================put file================")
        print("================   quit ===============")
        print("================Command================")

        cmd = input(">>>")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            # 因为输入文件下载的书写格式：get filename
            # cmd[:3] 表示取到了 关键字 "get"
            # cmd.split(' ') 基于空格进行分隔，cmd.split(' ')[-1]表示filename
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            # cmd.strip() 删除文件前后空格
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令")



if __name__ == '__main__':
    main()
