class BinaryTree:
    class Node:
        def __init__(self,data=None,left=None,right=None):
            self.data=data
            self.left=left
            self.right=right
            self.next=None
    def __init__(self):
        self.root=None
    def createsample(self)-> Node:
        self.root=self.Node(5)

        self.root.left=self.Node(3)
        self.root.right=self.Node(10)

        self.root.left.left=self.Node(1)
        self.root.left.right=self.Node(4)

        self.root.right.left=self.Node(8)
        self.root.right.right=self.Node(20)
        return self.root

    def preorder(self,root):
        if(root==None):
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def printsum(self,root):
        if(root==None):
            return 0
        return self.printsum(root.left)+self.printsum(root.right)+root.data

    def levelorder(self,root):
        if(root==None):
            return
        q=[root,None]
        while(q):
            val=q.pop()
            if(val==None):
                if(len(q)!=0):
                    print()
                    q.insert(0,None)
            else:
                print(val.data,end=" ")
                if(val.left!=None):
                    q.insert(0,val.left)
                if(val.right!=None):
                    q.insert(0,val.right)
    def fillnext(self,root):
        while(root!=None):
            nh,nt=None,None
            curr=root
            while(curr):
                print(curr.data)
                if(curr.left):
                    if(nh==None):
                        nh=nt=curr.left
                    else:
                        nt.next=curr.left
                        nt=nt.next

                if(curr.right):
                    if(nh==None):
                        nh=nt=curr.right
                    else:
                        nt.next=curr.right
                        nt=nt.next
                curr=curr.next
            root=nh
        print("done")
    def height(self, root):
        if(root==None):
            return 0
        
        return max(self.height(root.left),self.height(root.right))+1
    def topview(self,root,level,curr):
        if(root==None):
            return
        if(curr not in level):
            level[curr]=root.data
        self.topview(root.left,level,curr-1)
        self.topview(root.right,level,curr+1)
        return level
    def bottomview(self,root,levels,curr):
        if(root==None):
            return
        if(curr not in levels):
            levels[curr]=root.data
        else:
            levels[curr]=root.data

        self.bottomview(root.right,levels,curr+1)

        self.bottomview(root.left,levels,curr-1)
        
        return levels


obj=BinaryTree()
head=obj.createsample()
#obj.preorder(head)
#print(obj.printsum(head))
#obj.levelorder(head)
#obj.fillnext(head)
#print(head.left.left.next.next.data)
print(obj.height(head))
print(obj.topview(head,{},0))
print(obj.bottomview(head,{},0))
