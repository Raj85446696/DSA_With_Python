# We have to created singly Linkedlist.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # ------ insert at first position ------ # 
    def InsertAtFirst(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    # ------ insert at any position ------- # 
    def InsertatPosition(self,data,pos):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    #------- Insert at last position ---------#
    def InsertatLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next 
        temp.next = newNode
        newNode.next = None

    #------- delete at first position ----------#
    def DeleteFirst(self):
        if self.head is None:
            print("linkedlist not exits")
            return
        self.head = self.head.next 

    #-------- delete at any position ----------#
    
    def DeleteatanyPos(self,pos):
        temp = self.head
        if self.head is None:
            print("linkedlist not exits")
            return
        for i in range(1,pos-1):
            temp = temp.next
        temp2 = temp.next.next
        temp.next = temp2
        temp2.next = None

    #-------- delete at last position ----------#

    def Deletelast(self):
        temp = self.head
        if self.head is None:
            print("linkedlist not exits")
            return
        while temp.next.next is not None:
            temp = temp.next 
        temp.next = None

        

    #-------- Getting one by one element ---------#
    def Traverse(self):
        if self.head is None:
            print("Singly Linked list not exits")
            return
        temp = self.head 
        while temp is not None:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("null")
    
s = SinglyLinkedList()
s.InsertAtFirst(90)
s.InsertAtFirst(190)
s.InsertatPosition(23,1)
s.InsertatLast(55)
s.DeleteFirst()
s.DeleteatanyPos(1)
s.Deletelast()
s.Traverse()
