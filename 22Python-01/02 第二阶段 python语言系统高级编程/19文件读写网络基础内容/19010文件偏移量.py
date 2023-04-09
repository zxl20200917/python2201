"""
    文件偏移量
"""

f = open('file','w+')
f.write("hello world shijia")
# 由于文件对象f写入的操作，将文件写到末尾，所以下面的print输出就不会有任何信息。
# 如果要输出就需要把文件对象的偏移调整到开始的位置

print(f.tell())
# 把文件偏移量设置开始的位置
f.seek(0,0)
print(f.read())

f.close()

