import time
import random

while (True):
    time.sleep(random.randint(7, 8) / 100)
    f = open("./server/static/data.txt", 'r')
    line = f.readline()
    print(line)
    f.close()