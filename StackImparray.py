import numpy as np 
class Stack:
    def __init__(self):
        self.stack = np.array([])
    
    def display(self):
        temp = self.stack
        if temp is None:
            print("Stack : is empty")
            return
        for i in temp:
            print(i,end=" -> ")

s = Stack()
s.display()