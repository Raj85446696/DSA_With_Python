class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None 

    def addFirst(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        
    def PrintArray(self):
        currnode = self.head 
        while currnode:
            print(currnode.data,end=" -> ")
            currnode = currnode.next
    print("null")

l = Linkedlist()
l.addFirst(10)
l.addFirst(20)
l.addFirst(30)
l.addFirst(40)
l.addFirst(90)
l.PrintArray()

