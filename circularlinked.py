class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SingularLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insertfirst(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            return
        temp = self.head
        newNode.next = temp
        temp = newNode
        self.tail = newNode

    def InsertLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            return
        else:
            newNode = self.tail.next
            self.tail.next = newNode
        self.tail = newNode


    def Traverse(self):
        if self.head is None:
            print("linkedlist not exits")
            return 
        temp = self.head
        while temp is not None:
            print(temp.data,end=" <---> ")
            temp = temp.next
        print(temp)


s = SingularLinkedlist()
s.Insertfirst(90)
s.InsertLast(89)
s.Traverse()
