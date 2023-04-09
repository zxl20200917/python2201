"""

"""

from socket import *
import struct

# 和客户端一致
st = struct.Struct('i32sif')

# udp套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("127.0.0.1",8888))

# 打开文件
f = open("student.txt",'a')

while True:
    data,addr = s.recvfrom(1024)
    data = st.unpack(data)
    if not data:
        break
    # 写入文件
    info = "%d   %-10s   %s  %.1f\n" % (data[0],data[1].decode().strip('\x00'),data[2],data[3])
    f.write(info)
    f.flush()

f.close()
s.close()

