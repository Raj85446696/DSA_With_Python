 # type: ignore
class queue1:
    def __init__(self):
       self.value = [] 
    
    def enqueue(self,data):
       self.value.append(data)
    
    def dequeue(self):
       front = self.value[0]
       self.value = self.value[1:]
       return front
    
    def display(self):
       for i in range(0,len(self.value)):
          print(self.value[i],end=" <-- ")

q = queue1()
q.enqueue(90)
q.enqueue(190)
q.enqueue(290)
q.dequeue()
q.display()
