''' Implementing Queue using list 
Performing some Operation : Enqueue , Dequeue , size , front , rear  & display . 
'''
queue = [] 

def Enqueue(value):
    queue.append(value)
    print(f"Enqueue : {value}")

def Dequeue():
    elem = queue.pop(0)
    print(f"Dequeue : {elem}")

def size():
    print("Length of queue :",len(queue))

def front():
    print("Front value is : ",queue[0])

def rear(): 
    print("rear value is : ",queue[-1])
     

def display():
    if len(queue)==0:
        print("queue not exits..")
        return
    for i in queue:
        print(i,end=" <- ")

Enqueue(90)
Enqueue(190)
Enqueue(290)
Dequeue()
size()
front()
rear()
display()
