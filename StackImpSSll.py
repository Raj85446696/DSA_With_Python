class Stack:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackImpSSll:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def Push(self,data):
        newStack = Stack(data)
        if self.front is None:
            self.front = newStack
            return
        newStack.next = self.front
        self.front = newStack

    def Pop(self):
        if self.front is None:
            print("Stack : UnderFlow")
            return
        self.front = self.front.next

    def display(self):
        if self.front is None:
            print("Stack does't exits.")
            return
        temp = self.front
        while temp is not None:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

s = StackImpSSll()
s.Push(90)
s.Push(190)
s.Push(290)
s.Pop()
# s.Pop()

s.display()