"""
    从终端使用input输入一个文件位置，通过文件读写操作复制一份该文件。
    注意：这个文件可能是文本文件也可能是二进制文件
"""

# 输入文件名
# 测试输入的文件是：../18Python操作Mysql数据库/1.jpg 图片，二进制文件
# 生成本地文件为:file.jpg
filename = input("File:")

try:
    fr = open(filename,'rb')
except FileNotFoundError as e:
    print(e)
else:
    fw = open('file.jpg','wb')
    # 循环读取文件直到最后
    while True:
        data = fr.read(1024)
        # 文件结束
        if not data:
            break
        # 将读取内容写入
        fw.write(data)
    fr.close()
    fw.close()
