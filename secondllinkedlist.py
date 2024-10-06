class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    #------Insert at First Position -------# 

    def FirstInsert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    #------Insert at any Position -------# 
    def InsertatPosition(self,data,pos):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next 
        temp2 = temp.next
        newNode.next = temp2
        temp.next = newNode
        temp2.prev = newNode
        temp.next = newNode
    

    def Traversal(self):
        if self.head is None:
            print("Doublylinked list not exits.")
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end=" <--> ")
            temp = temp.next
        print("null")

d = DoublyLinkedlist()
d.FirstInsert(190)
d.FirstInsert(90)
d.InsertatPosition(2,23)
d.Traversal()