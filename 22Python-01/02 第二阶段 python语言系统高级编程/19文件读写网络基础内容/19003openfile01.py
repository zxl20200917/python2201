"""
    打开文件
"""

f = open('../18Python操作Mysql数据库/1.jpg', 'rb')

# 由于不清楚打开的数据多少，所以直拉采用一直循环的模式输出数据
# read演示
# while True:
#     data = f.read(2)
#     # 读取数据后，最后会输入null空字符，所以作为判断条件，当非数据为真时，跳出循环
#     if not data:
#         break
#     print(data)
# f.close()

# readline演示
# while True:
#     data = f.readline()
#     if not data:
#         break
#     print(data)
#
#
# f.close()


# while True:
#     data = f.readlines(2)
#     if not data:
#         break
#     print(data)
#
# f.close()


# 第4种方式读取文件
for line in f:
    print(line)

f.close()