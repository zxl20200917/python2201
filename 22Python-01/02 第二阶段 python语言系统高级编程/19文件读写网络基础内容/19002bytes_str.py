s = "hello word"
str = "你好"

# 字符串转换为字节串
b01 = str.encode()
bytes = s.encode()
print(b01)
print(bytes)

# 字节串转换为字符串
print(b01.decode())
print(bytes.decode())