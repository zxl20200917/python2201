"""
    writeline写入操作
"""

list = ["hello","word","zhangxuelong"]

f = open("file ","a")

for i in range(len(list)):
    f.write('\n')
    f.writelines(list[i])

f.close()
