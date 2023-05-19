# 循环取值(遍历)
# 列表、字典、字符串、元组、聚合

"""
    for  变量名  in 可迭代对象：
        子代码块
"""
# # 第一
# l = ['张大仙', '张宠发', '张交心', '张坦克']
# for a in l:
#     print(a)
#
# i = 0
# while i < 4:
#     print(l[i])
#     i += 1
#
# # 操作字典
# dic = {'name':'张大人','age':84,'height':200}
#
# for i in dic:
#     print(dic)
#     print(dic[i])
#
# # 操作字符串
# s = 'hello world'
# for i in s:
#     print(i)

# # 用for循环固定字符串
# for x in [1,2,3,4,5]:
#     print('aaa')
#     # 打印5次'aaa'
#
#
# # for-range操作
# for i in range(0,9,2):
#     print(i)
#
#
# for i in range(10):
#     print('外层循环--->',i)
#     for j in range(1,10):
#         print('内层循环--->',j)

# 用for循环打印九九乘法表
# print默认是换行\n， 如果去掉默认换行符的话，end=' '，如果是制表符的话如：end= '\t'
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j} x {i} = {i*j}',end='\t')
    print(' ')
