"""
    fork使用
"""

import os,sys

pid = os.fork()
# 执行这个时，就会创建子进程与此父进程所以代码是一样的
# 而父进程返回值是子进程的PID号，所以是大于0的，执行的结果是 "the old process" "fork test over"
# 而子进程执行的时候是从pid = os.fork()下一句开始的。
# 而由于子进程的返回值是0，这个是规定的
# 所以子进程执行结果是："the new process" "fork test over"

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("the new process")
else:
    print("the old process")

print("fork test over")
