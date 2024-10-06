class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
class DobleyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertFirst(self,data):
        newNode = Node(data)
        temp = self.head 
        
        if (temp ==None):
            self.head = self.tail = newNode
            return
        while (temp != None):
            temp.prev = newNode
            newNode.next = temp
            newNode.prev = None
            temp = newNode
        print("null")


    def Traverse(self):
        temp = self.head 
        if (temp == None):
            print("linkedlist Not exits.")
            return
        while (temp != None):
            print(temp.data,end=" <--> ")
            temp = temp.next 
        print("null")

dl = DobleyLinkedList()
dl.InsertFirst(90)
dl.InsertFirst(123)
dl.Traverse()


