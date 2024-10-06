queue = list()

def Enqueue():
    num = int(input("enter a number :- "))
    queue.append(num)
    print(f"{num} element added to queue")

def Dequeue():
    if len(queue)>0:
        rem = queue.pop(0)
        print(f"{rem} element remove to queue")
    else:
        print("queue is empty")

def display():
    if len(queue)>0:
        print("Queue Elements : ")
        for i in queue:
            print(i)
    else:
        print("queue is empty")

while True:
    print("""Enter your option:
          1.Enqueue
          2.Dequeue
          3.Display
          4.Exit
""")
    op = int(input("enter a operation :- "))
    if op==1:
        print("option 1: Selected Successfully ")
        Enqueue()
    elif op==2:
        print("option 2: Selected Successfully ")
        Dequeue()
    elif op ==3:
        print("option 3: Selected Successfully ")
        display()
    elif op == 4:
        print("Exiting . . .")
        break
    else:
        print("enter correct option ")

