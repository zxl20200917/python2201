"""
    struct
"""

import struct

## 第一种用法
# 1 lily 18 1.65

# fmt = "i4sif"
#
# st = struct.Struct(fmt)
#
# data = st.pack(1,b'lily',18,1.65)
# # 此时data是个可以应用任何编程语言中，就可以应用其他编程语言编程中
# print(data)
#
# msg = st.unpack(data)
# print(msg)

# 第二种用法，直接生成可应用其他编程语言的数据
data = struct.pack("i4sif",1,b'lily',18,1.66)
print(data)

msg = struct.unpack("i4sif",data)
print(msg)

