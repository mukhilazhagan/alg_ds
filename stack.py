# Implementing a Stack ADT class using Lists 

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == [] ## is the list equal to an empty list
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[ len(self.items) - 1 ]
    
    def size(self):
        return len(self.items)