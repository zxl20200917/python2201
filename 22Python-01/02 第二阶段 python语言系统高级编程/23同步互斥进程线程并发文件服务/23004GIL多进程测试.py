import multiprocessing

from test import *
from multiprocessing import Process
import time

jobs = []

tm = time.time()

def main():
    for i in range(10):
        p = Process(target=io)
        # p = Process(target=count(1,1))

        jobs.append(p )
        p.start()

    for i in jobs:
        i.join()

    print("Thead io:",time.time() - tm)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()