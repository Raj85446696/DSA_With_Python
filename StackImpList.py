class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        temp = self.stack
        if temp is None:
            temp.insert(0,data)
            return
        temp.append(data)

    def Pop(self):
        temp = self.stack
        if temp is None:
            print("Stack : UnderFlow")
            return
        temp.pop()
        return
            

    def display(self):
        if len(self.stack)==0:
            print("Queue does't exits.")
            return 
        for i in self.stack:
            print(i,end=" -> ")

s = Stack()
s.push(99)
s.push(199)
s.push(299)
s.Pop()
# s.Pop()
s.Top()
s.display()
