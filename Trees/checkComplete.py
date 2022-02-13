class Tree:


    class Node:


        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right

    def createTree(self):
        root = self.Node("A")
        root.left = self.Node("B")
        root.right = self.Node("C")

        root.left.left = self.Node("D")
        root.left.right = self.Node("E")

        root.right.left = self.Node("F")
        root.right.right = self.Node("G")
        return root
    
    def countNodes(self,r):
        if(r == None):
            return 0
        return self.countNodes(r.left) + self.countNodes(r.right) + 1

    def height(self,r):
        if(r == None):
            return 0
        return max(self.height(r.left),self.height(r.right))+1
    
    
    def preOrder(self,r):
        if(r==None):
            return
        print(r.val,end=" ")
        self.preOrder(r.left)
        self.preOrder(r.right)
    
    
    def inOrder(self,r):
        if(r==None):
            return
        self.inOrder(r.left)
        print(r.val,end=" ")
        self.inOrder(r.right)


    def postOrder(self,r):
        if(r==None):
            return
        self.postOrder(r.left)
        self.postOrder(r.right)
        print(r.val,end=" ")


obj = Tree()
root = obj.createTree()
n= obj.countNodes(root)
h = obj.height(root)
if(n == (2**h) - 1):
    print("complete")
else:
    print("not complete")
obj.preOrder(root)
print()
obj.inOrder(root)
print()
obj.postOrder(root)


