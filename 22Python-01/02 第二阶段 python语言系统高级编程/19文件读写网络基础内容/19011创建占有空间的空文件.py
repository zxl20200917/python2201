"""
    创建空洞文件
"""

f = open('file03','wb')
f.write(b'a')
f.seek(1024)
f.write(b'b')

f.close()