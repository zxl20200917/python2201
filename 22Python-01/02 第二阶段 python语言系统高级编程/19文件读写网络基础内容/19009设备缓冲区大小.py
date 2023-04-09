"""
    设备缓冲区大小
"""
# 设置缓冲区的大小为5个字节，超过来5个字节自动从缓冲区存储到磁盘文件中
# f = open('file','wb',5)
# while True:
#     data = input(">>>>")
#     if not data:
#         break
#     f.write(data.encode())
# f.close()

# 设置缓冲区为行缓冲，就是遇到换行就会自动从缓冲区写到磁盘中去
# f = open('file01', 'w', 1)
# while True:
#     data = input(">>>>")
#     if not data:
#         break
#     f.write(data + '\n')
# f.close()


# 采用系统默认的缓冲区，并采用函数刷新缓冲区
f = open('file02', 'w', 1)
while True:
    data = input(">>>>")
    if not data:
        break
    f.write(data + '\n')
    # 调用flush()进行刷新缓冲
    f.flush()
f.close()