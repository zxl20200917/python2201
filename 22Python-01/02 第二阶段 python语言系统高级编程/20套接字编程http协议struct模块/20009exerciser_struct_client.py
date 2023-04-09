"""

"""

from socket import *
import struct

# 数据格式
st = struct.Struct('i32sif')

# udp套接字
s = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',8888)

while True:
    print("==============================")
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("Age:"))
    score = float(input('Score:'))
    # 打包数据发送
    data = st.pack(id,name,age,score)
    if not data:
        break
    s.sendto(data,ADDR)

s.close()
