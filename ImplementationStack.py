# # Implementation of Stack using list.
# class Stack:
#     def __init__(self):
#         self.stack = []

#     # Push -> This Method are used to insert the element at Top in stack.
#     def Push(self,value):
#         if len(self.stack)==0:
#             self.stack.insert(0,value)
#             # print(value,"Element added to Stack.")
#             return
#         self.stack.append(value)
#         # print(value,"Element added to Stack.")

#     # Pop -> This Method are used to remove the element at top in stack.
#     def Pop(self):
#         if len(self.stack)==0:
#             print("Stack :- UnderFlow")
#             return
#         top = self.stack.pop(0)
#         print(top,"Element remove to Stack.")

#     def display_stack(self):
#         if len(self.stack)==0:
#             print("Stack : does't exit.")
#             return
#         for i in self.stack:
#             print(i)



# s = Stack()
# s.Push(9)
# s.Push(19)
# s.Push(29)
# s.Push(39)
# s.Push(49)
# s.Pop()
# s.Pop()
# print(" ")
# s.display_stack()

# Implementation of Stack using Linkedlist.
class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None

class Stack:
    def __init__(self):
        self.head = None


    def Push(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.nref = self.head
        self.head = newNode

    def Pop(self):
        if self.head is None:
            print("Stack : UnderFlow.")
            return
        self.head =self.head.nref

    # def Peak(self):
    #     top = self.head.data
    #     print(top)


    def display(self):
        if self.head is None:
            print("Stack : not Exits")
            return
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.nref

s = Stack()
s.Push(99)
s.Push(199)
s.Push(299)
s.Push(399)
s.Push(499)
s.Pop()
# s.Pop()
# s.Pop()
s.display()
s.Peak()



    