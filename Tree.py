# creating a Binary Tree
class Node:
    def __init__(self,data):
        self.leftChild = None
        self.data = data
        self.rightChild = None

    def Insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data<self.data:
                if self.leftChild is None:
                    self.leftChild = Node(data)
                    return
                else:
                    self.leftChild.Insert(data)
            elif data>self.data:
                if self.rightChild is None:
                    self.rightChild = Node(data)
                    return
                else:
                    self.rightChild.Insert(data)

    #----------- Searching a Node --------------#
    def Search(self,data):
        if self.data == data:
            print("Node Found!")
            return
        elif data<self.data:
            if self.leftChild is None:
                print("LeftChild Empty")
                return
            else:
                self.leftChild.Search(data)
        elif data>self.data:
            if self.rightChild is None:
                print("RightChild Empty!")
                return
            else:
                self.rightChild.Search(data)

    #--------- Deleting a Node -----------#
    def Delete(self,data):
        if self.data is None:
            print("Tree Does't Exits.")
            return
        elif data<self.data:
            if self.leftChild:
                self.leftChild = self.leftChild.Delete(data)
            else:
                print("Left child not exits")
        elif data>self.data:
            if self.rightChild:
                self.rightChild = self.rightChild.Delete(data)
            else:
                print("Right Child not exits.")
        else:
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            if self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            
            temp = self.rightChild

            while temp.leftChild:
                temp = temp.leftChild
            self.data = temp.data
            self.rightChild = self.rightChild.Delete(temp.data)
        return self


    def Inorder(self):
        if self.leftChild:
            self.leftChild.Inorder()
        print(self.data,end=" ")
        if self.rightChild:
            self.rightChild.Inorder()
    
    def Preorder(self):
        print(self.data,end=" ")
        if self.leftChild:
            self.leftChild.Preorder()
        if self.rightChild:
            self.rightChild.Preorder()
    
    def Postorder(self):
        if self.leftChild:
            self.leftChild.Postorder()
        print(self.data,end=" ")
        if self.rightChild:
            self.rightChild.Postorder()


root = Node(12)
root.Insert(10)
root.Insert(20)
root.Insert(30)
root.Insert(90)
root.Inorder()
print(" ")
root.Preorder()
print(" ")
root.Postorder()
print("")
root.Search(90)
print("")
root.Delete(30)
root.Inorder()