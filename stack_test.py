# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:07:42 2019

@author: mukhi
"""


import time
import stack
#import paranthesis_checker_stack
from paranthesis_checker_stack import *

#s= Stack()
#
#start = time.time()
#
#print(s.isEmpty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.isEmpty())
#s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())
#
#end = time.time()

#print("time elapesed :", end-start)

print(anyParChecker('[]'))
print(anyParChecker('{({([][])})}'))
print(anyParChecker('[{()]'))