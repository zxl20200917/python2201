"""
    while循环
"""

username = '111'
password = '123456'

# condition = True

#
# while condition:
#     input_username = input('请输入你的帐号：')
#     input_password = input('请输入你的密码：')
#     if input_username == username and input_password == password:
#         print('登录成功')
#         condition = False
#     else:
#         print('用户名或者密码错误')
#

# condition = True


# while True:
#     input_username = input('请输入你的帐号：')
#     input_password = input('请输入你的密码：')
#     if input_username == username and input_password == password:
#         print('登录成功')
#         #  break只退出本循环
#         while True:
#             action = input('请输入你的操作：')
#             if action == 'Q':
#                 break
#             print(f'正在{action}')
#         break
#     else:
#         print('用户名或者密码错误')

# while+contiue
# 打印除4的所以数
num = 0
while num < 10:
    if num == 4:
        num += 1
        continue
    print(num)
    num +=1

# while + else

# while True:
#     input_username = input('请输入你的帐号：')
#     input_password = input('请输入你的密码：')
#     if input_username == username and input_password == password:
#         print('登录成功')
#         #  break只退出本循环
#         while True:
#             action = input('请输入你的操作：')
#             if action == 'Q':
#                 break
#             print(f'正在{action}')
#         break
#     else:
#         print('用户名或者密码错误')



