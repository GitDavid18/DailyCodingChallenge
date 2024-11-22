# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time


class scheduler:
    def __init__(self, n, f):
        self.timeout = n
        self.function = f

    def execute(self):
        time.sleep(self.timeout/1000)
        self.function(self.timeout)


def printMe(time):
    print("Executing after timeout of " + str(time) + "ms")


func = printMe
x = scheduler(5000, func)
x.execute()
