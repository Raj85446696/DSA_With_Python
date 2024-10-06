class Node:
    def __init__(self,value):
        self.pref = None
        self.value = value
        self.nref = None
    
class doublyLinkedlist:
    def __init__(self):
        self.head = None

    #----------- Insert at First Position -----------#

    def InsertFirst(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return

        newNode.nref = self.head
        self.head.pref = newNode
        self.head = newNode

    #----------- Insert at any Position -----------#

    def InsertatPos(self,value,pos):
        newNode = Node(value)
        temp = self.head
        if self.head is None:
            self.head = newNode
            return
        
        for i in range(0,pos-1):
            temp = temp.nref
        newNode.nref = temp.nref
        newNode.pref = temp
        temp.nref = newNode
        temp.nref.pref = newNode

    #----------- Insert at last Position -----------#  
    def InsertLast(self,value):
        newNode = Node(value)
        temp = self.head
        if self.head is None:
            self.head = newNode
            return
        while temp.nref is not None:
            temp = temp.nref
        temp.nref = newNode
        newNode.pref = temp
        newNode.nref = None

    #----------- Delete at first Position -----------# 
    def DeleteFirst(self):
        if self.head is None:
            print("not any node present.")
            return
        self.head = self.head.nref
        self.head.pref = None
    
    #----------- Delete at any Position -----------# 
    def DeleteanyPos(self,pos):
        if self.head is None:
            print("not any node present.")
            return
        temp = self.head
        for i in range(0,pos-1):
            temp = temp.nref 
        temp2 = temp.nref.nref
        temp.nref = None
        temp.nref = temp2
        temp2 = temp

    #----------- Delete at last Position -----------# 
    def DeleteLast(self):
        if self.head is None:
            print("not any node present.")
            return
        temp = self.head
        while temp.nref.nref is not None:
            temp = temp.nref
        temp.nref = None


    #----------- Traversal of linkedlist -----------#

    def Traverse(self):
        if self.head is None:
            print("linkedlist not exits")
            return
        temp = self.head
        while temp is not None:
            print(temp.value,end=" <-> ")
            temp = temp.nref
        print("null")



d = doublyLinkedlist()
d.InsertFirst(90)
d.InsertFirst(190)
d.InsertatPos(234,1)
d.InsertLast(345)
d.InsertatPos(999,3)
d.DeleteFirst()
d.DeleteanyPos(2)
d.DeleteLast()
d.Traverse()