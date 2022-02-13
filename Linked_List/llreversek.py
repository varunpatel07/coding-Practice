class LinkedList:
    class Node:
        def __init__(self,val):
            self.data=val
            self.next=None
        
    def __init__(self):
        self.head=None
    
    def create(self):
        self.head=self.Node(1)
        self.head.next=self.Node(2)
        #self.head.next.next=self.Node(3)
        #self.head.next.next.next=self.Node(4)
        #self.head.next.next.next.next=self.Node(5)
        #self.head.next.next.next.next.next=self.Node(6)
        #self.head.next.next.next.next.next.next=self.Node(7)
        #self.head.next.next.next.next.next.next.next=self.Node(8)
        #self.head.next.next.next.next.next.next.next.next=self.Node(9)
        return self.head

    def display(self,head):
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
    def reverse(self,head,k):
        nh=None
        nt=head
        ls=None
        while(head!=None and k!=0):
            curr=head
            ls=head.next
            head=head.next
            curr.next=nh
            nh=curr
            k-=1
        nt.next=ls
        return [nh,nt]
    def reversek(self,head,k):
        if(head==None):
            return head
        mh,mt=self.reverse(head,k)
        head=mt.next
        while(head!=None):
            ch,ct=self.reverse(head,k)
            mt.next=ch
            mt=ct
            head=ct.next
        return mh
        

obj=LinkedList()
head=obj.create()
#obj.display(head)
obj.display(obj.reversek(head,3))