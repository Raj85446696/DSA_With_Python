class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularSinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    #-------- Insert At Beginning --------#
    def InsertAtBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
            return
        newNode.next = self.head
        self.tail.next = newNode
        self.head = newNode
    
    #-------- Insert At any Position --------#
    def InsertatPos(self,data,pos):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
            return
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next 
        temp2 = temp.next
        newNode.next = temp2
        temp.next = newNode

    
    #-------- Insert At Last Position --------#
    def InsertLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.tail.next = self.head
            return
        self.tail.next = newNode
        newNode.next = self.head
        self.tail = newNode
        
    #-------- Delete At First Position --------#
    def DeleteFirst(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        temp = self.head 
        self.head = self.head.next 
        self.tail.next = self.head
        temp = None
    
    def Deletelast(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next 

        temp.next = self.head
        self.tail = temp


    def display(self):
        if self.head is None:
            print("CircularLinkedList Not Exists..")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:  # Stop when we reach the head again
               break
        print()  # For a newline after the list display

        


c = CircularSinglyLL()
c.InsertAtBegin(90)
c.InsertAtBegin(190)
c.InsertAtBegin(290)
c.InsertatPos(400,2)
c.InsertatPos(520,1)
c.InsertLast(900)
c.DeleteFirst()
c.Deletelast()
c.display()