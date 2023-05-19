"""
    字符串详解
"""
# 索引取值
info = "good good study,day day up"

print(info[5])
print(info[-1])

# 切片
print(info[0:4])
print(info)
print(info[:-1])
print(info[:4])
print(info[0:20:3])
print(info[4:0:-1])

# strip 去除空格左右两端

name = '  张大仙'
print(name.strip())
# 如果两个有很多其他要去除的字符如以把字符写到strip里
name1 = 'adf*  张大仙 def'
print(name1.strip('abcdef*'))

print(name.rstrip())
print((name.lstrip()))

# split拆分
# 默认依据空格返回一个列表

names = '李白 进食  路南  孙司空'
print(names.split())
print(names.split(' ', 1))


# len  长度
print(len(info))


# lower upper
msg = 'ABCdef'
print(msg.lower())
print(msg.upper())

# 成员运算in和not in
print('张大仙' in info)


# startswith endswith 依据字符串开头或者结尾
print('君不见，黄河镇，abc'.startswith('君不见'))
print('君不见，黄河镇，abc'.endswith('abc'))


# join 拼接
l = ['李白','白聚义','独步']
print('-'.join(l))

# replace
name2 = '李白-白聚义-独步'
print(name2.replace('-', ':', 1))
print(name2.replace('李白', '诗仙', 1))


# isdigit 判断字符串是事为数字
print('84'.isdigit())

