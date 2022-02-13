class LinkedList:
    class Node:
        def __init__(self,val):
            self.data=val
            self.next=None
        
    def __init__(self):
        self.head=None
    
    def create(self):
        self.head=self.Node('A')
        self.head.next=self.Node('B')
        #self.head.next.next=self.Node('C')
        #self.head.next.next.next=self.Node('D')
        #self.head.next.next.next.next=self.Node('B')
        #self.head.next.next.next.next.next=self.Node('A')
        return self.head

    def display(self,head):
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
        
    def findmid(self,head):
        slow,fast=head,head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow

    def reverse(self,node):
        nh=None
        while(node!=None):
            nn=node
            node=node.next
            nn.next=nh
            nh=nn
        return nh
    def checkpalindrome(self,head):
        if(head==None or head.next==None):
            return True
        mid=self.findmid(head)
        mid=self.reverse(mid)
        while(mid!=None):
            if(head.data!=mid.data):
                return False
            head=head.next
            mid=mid.next
        return True

obj=LinkedList()
head=obj.create()
#obj.display(head)
#print()
#obj.display(obj.reverse(obj.findmid(head)))
print(obj.checkpalindrome(head))