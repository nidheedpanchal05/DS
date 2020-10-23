# Practical 8

class Node():
    def __init__(self,val,right=None,left=None):
        self.val = val
        self.right = right
        self.left = left

    def printInorder(self):
        if self.val:
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
            
    def printPreorder(self):
        if self.val:
            print(self.val)
            if self.left:
                self.left.printPreorder()
            if self.right:
                self.right.printPreorder()


root1 = Node(62)
root1.left = Node(1)
root1.right = Node(101)
root1.left.right = Node(7)
root1.left.right.right = Node(15)
root1.right.right = Node(102)

print("-----InOrder-----")
root1.printInorder()
print("----PostOrder----")
root1.printPostorder()
print("-----PreOrder----")
root1.printPreorder()


        
