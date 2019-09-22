# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:11:39 2019

@author: mukhi
"""
from stack import *

def parChecker(par_str):
    
    s = Stack()
    balanced = True
    index = 0
    
    while index != len(par_str) and balanced:
        symbol = par_str[index]
        
        if( symbol == '('):
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()     
        
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
def anyParChecker(par_str):
    
    s = Stack()
    balanced = True
    index = 0
    
    while index != len(par_str) and balanced:
        symbol = par_str[index]
        
        if( symbol in '({['):
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                balanced = compareBrackets(top, symbol)
                
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
            
def compareBrackets(a, b):
    open_str = '([{'
    close_str = ')]}'
    return open_str.index(a) == close_str.index(b)