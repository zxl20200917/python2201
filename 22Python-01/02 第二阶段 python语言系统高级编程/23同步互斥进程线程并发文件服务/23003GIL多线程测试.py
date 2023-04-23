from test import *
from threading import Thread
import time

jobs = []

tm = time.time()

for i in range(10):
    # t = Thread(target=io)
    t = Thread(target=count(1,1))

    jobs.append(t )
    t.start()

for i in jobs:
    i.join()

print("Thead io:",time.time() - tm)