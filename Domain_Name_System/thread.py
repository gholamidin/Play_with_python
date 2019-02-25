#!/usr/bin/python3

#compare for multi threads

import time
import threading
def worker():
    print("worker")
    time.sleep(1)
    return


#   for i in range(20):
#       worker()

for i in range(20):
    t = threading.Thread(target = worker)
    t.start()
