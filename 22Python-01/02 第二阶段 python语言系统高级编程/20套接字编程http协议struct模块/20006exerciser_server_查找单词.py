"""
    查找单词
    从客户端使用input输入一个单词，发送给客户端，服务端基于单词本找以该单词，将单词和单词解释回发给客户端，
    由客户端打印出来。
"""

from socket import *


# 定义查找单词的函数
def find_word(word):
    f = open('../18Python操作Mysql数据库/dict.txt')
    for line in f:
        w = line.split(' ')[0]
        # 如果遍历到了单词已经大于word就结束查找
        if w > word:
            f.close()
            return
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return


# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ('0.0.0.0', 8009)
sockfd.bind(server_addr)

while True:
    # data接收到的单词
    data, addr = sockfd.recvfrom(1024)
    # if not data:
    #     break
    # 查单词
    result = find_word(data.decode())
    sockfd.sendto(result.encode(),addr)

# 关闭套接字
sockfd.close()
