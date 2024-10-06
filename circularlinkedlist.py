class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def Traverse(self):
        
