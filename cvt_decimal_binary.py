
from stack import *

def cvt_decToBin(decNum):

    reminder_stack = Stack()

    while decNum > 0:

        rem = decNum%2
        reminder_stack.push(rem)
        decNum = decNum // 2

    binaryString = ""

    while not reminder_stack.isEmpty():
        binaryString = binaryString + str( reminder_stack.pop() )

    return binaryString

