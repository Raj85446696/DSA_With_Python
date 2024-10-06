''' Create a Circular Singly Linkedlist and perform Certain operation 
    1. Insertion --> i) Begin ii) at position iii) at end.
    2. Deletetion--> i) Begin ii) at position iii) at end.
    3. Traversing / Display the element of linkedlist.
'''

class Node: # Create a node class 
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    #-----1. i) Insert at begining -----#
    
    def InsertatBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
            return
        newNode.next = self.head
        self.tail.next = newNode
        self.head = newNode

    #-----1. ii) Insert at any Position -----#
    def InsertatPosition(self,data,pos):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
            return
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    
    #-----1. iii) Insert at Last -----#
    def InsertatLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
            return
        self.tail.next = newNode
        newNode.next = self.head
        self.tail = newNode
    
    #-----2. i) Delete at Begin -----#
    def DeleteFirst(self):
        if self.head is None:
            return None
        self.head = self.head.next
        self.tail.next = self.head
    
    #-----2. ii) Delete at anyPosition -----#
    def DeletePosition(self,pos):
        if self.head is None:
            return None
        temp = self.head
        for i in range(pos-1):
            temp = temp.next 
        temp.next = temp.next.next

    #-----2. iii) Delete at Last-Position -----#
    def Deletelast(self):
        if self.head is None:
            return None
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head 

    
          

    #----- Traversing of Linkedlist -----#
    def Traverse(self):
        if self.head is None:
            print("CircularSinglyLinkedList don't exits.")
            return
        temp = self.head
        while True:
            print(temp.data , end=" -->> ")
            temp = temp.next
            if temp == self.head:
                break
    
c = CircularSinglyLinkedList()
c.InsertatBegin(90)
c.InsertatBegin(190)
c.InsertatBegin(490)
c.InsertatPosition(450,2)
c.InsertatLast(34)
c.DeleteFirst()
c.DeletePosition(1)
c.Deletelast()
c.Traverse()

