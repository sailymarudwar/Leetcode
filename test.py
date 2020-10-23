'''class Testing:
    def __init__(self):
        self.__score = 95

    def test(self):
        print("Score {}".format(self.__score))

    def ms(self,score):
        self.__score = score
        print("Max score: {}".format(self.__score))

results = Testing()
print(results.test())

print(results.ms(100))
print(results.test())'''

import sys, traceback, pdb

def lumberjack():
    bright_side_of_death()

def bright_side_of_death():
    return tuple()[0]
def debug(e, i, tb):
    traceback.print_exception(e, i, tb)
    pdb.pm()

try:
    lumberjack()
except IndexError:
    e, i, tb = sys.exc_info()
    traceback.excepthook = debug(e, i, tb)



