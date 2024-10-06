''' Implementing Queue using Singlylinkedlist
Performing some Operation : Enqueue , Dequeue , size , front , rear  & display . 
'''

class Node: 
    def __init__(self,data):
        self.data = data
        self.ref = None

class QueueSS:
    def __init__(self):
        self.front= None
        self.rear = None

    def Enqueue(self,data):
        newQueue = Node(data)
        if self.front is None:
            self.front = self.rear = newQueue
            return
        self.rear.ref = newQueue
        self.rear = newQueue

    def Dequeue(self):
        if self.front is None:
            print("UnderFlow: Queue")
            return
        self.front = self.front.ref

    def Display(self):
        if self.front is None:
            print("Queue is not exits")
            return
        temp = self.front
        while temp is not None:
            print(temp.data,end=" <-- ")
            temp = temp.ref
        print("null")

q = QueueSS()
q.Enqueue(45)
q.Enqueue(9)
q.Enqueue(19)
q.Dequeue()
q.Display()