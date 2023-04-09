"""
    tcp服务端流程
"""

# 创建tcp套接字
import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8000))

# 设置监听
sockfd.listen(3)

# 有客户端触发##时connfd连接就会退了，但是不让服务端退出， 只能把连接重新加入到循环中，不停循环等待客户端的接入
# 但是此循环必须要有退出机制，也就是退出异常捕捉后进行break退出，不然sockfd.close此代码就会失效，原因是没有退出
# 机制就代码 就不会执行此句代码。
while True:
    # 等待处理客户端连接
    print("waiting for connect....")
    try:
        connfd, addr = sockfd.accept()
        print("connect from ", addr)
    except Exception as e:
        print(e)
        break

    # 收发消息
    while True:
        data = connfd.recv(1024)
        print("Receive", data.decode())
        # 这部分主要由于基于客户端发送过来的特殊字符##来退出，但是服务端一般不退出，
        # 所以就把需要把connfd连接服务也加入到循环中。
        if data == b'##':
            break
        n = connfd.send(b'thanks')
        print("send %d bytes" % n)

    # 关闭套接字
    connfd.close()

sockfd.close()
