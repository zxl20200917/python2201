"""
    僵尸进程产生
"""

import os

pid = os.fork()

if pid <0:
    print("Error")
elif pid == 0:
    print("child process:",os.getpid())
else:
    while True:
        pass