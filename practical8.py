# Practical 8
'''
Preorder
Inorder
Postorder
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self,data):
       if self.val:
           if data < self.val:
               if self.left is None:
                   self.left = Node(data)
               else:
                    self.left.insert(data)
           elif data>self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
       else :
            self.val = data

    def PrintTree(self):
        if  self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


    def printPreorder(self):
        if self.val:
            print(self.val)
            if self.left:
                self.left.printPreorder()
            if self.right:
                self.right.printPreorder()
                
    
    
    def  printInorder(self):
        if self.val :
            if self.left:
                self.left.printInorder()
            print(self.val)
            if self.right:
                self.right.printInorder()

    def printPostorder(self):
        if self.val:
            if self.left:
                self.left.printPostorder()
            if self.right:
                self.right.printPostorder()
            print(self.val)


root = Node(62)
root.left = Node(1)
root.right = Node(101)
root.left.right = Node(7)
root.left.right.right = Node(15)
root.right.right = Node(102)

print('Without any ordering')
root.PrintTree()

print('now ordering with insert and printing' )
root1 = Node(62)
root1.insert(1)
root1.insert(7)
root1.insert(15)
root1.insert(101)
root1.insert(102)
root1.PrintTree()

print("Inorder".center(50,'-'))
root1.printInorder()

print("Preorder".center(50,'-'))
root1.printPreorder()

print("Postorder".center(50,'-'))
root1.printPostorder()

        
