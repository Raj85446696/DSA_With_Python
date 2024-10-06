queue = list()

def Display():
    if len(queue)>0:
        print("Elements are :- ")
        for i in queue:
            print(i)
    else:
        print("queue not exits")
    
def Enqueue():
    num = int(input("enter a number = "))
    queue.append(num)
    print(f"{num} : Element added to Queue.")

def Dequeue():
    if len(queue)>0:
        rem = queue.pop(0)
        print(f"{rem} : Element Remove to Queue")



while True:
    print(""" Menu : Enter Your Operation 
          1.Display
          2.Enqueue
          3.Dequeue
          4.Exit
""")
    op = int(input("enter a operation :- "))
    if op == 1:
        print("Operation 1 : Selected Successfully")
        Display()
    elif op ==2:
        print("Operation 2 : Selected Successfully")
        Enqueue()
    elif op ==3:
        print("Operation 3 : Selected Successfully")
        Display()
    elif op ==4:
        print("Exiting.......")
        break
    else:
        print("enter correct operation.")
        
