# from thereding import *
import threading

class thrd1:
    def car(self):
        for i in range(1, 100):
            print("aabbbccc")



class thrd2:
    def car(self):
        for i in range(1, 100):
            print("xxyyzz")

obj1 = thrd1()
obj2 = thrd2()


# obj1.car()
# obj2.car()

my_thread = threading.Thread(target=obj1.car)
my_thread1 = threading.Thread(target=obj2.car)



my_thread.start()
# my_thread1.start()

from time import sleep


# sleep(10)
print("oooooooooooooooooooo")


import time


timee = time.perf_counter()

