#find maximum sum of k nodes in a linked list
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
        self.head.next.next=self.Node(3)
        self.head.next.next.next=self.Node(4)
        self.head.next.next.next.next=self.Node(25)
        self.head.next.next.next.next.next=self.Node(6)
        self.head.next.next.next.next.next.next=self.Node(7)
        self.head.next.next.next.next.next.next.next=self.Node(8)
        self.head.next.next.next.next.next.next.next.next=self.Node(9)
        return self.head


    def display(self,head):
        while(head!=None):
            print(head.data,end=" ")
            head=head.next

    def findmaxsum(self,head,k):
        ms=0
        ws=0
        end=head
        while(k!=0 and head!=None):
            ws+=head.data
            head=head.next
            k-=1
        if(k!=0 or head==None):
            return 0
        while(head!=None):
            ws=ws-end.data+head.data
            
            ms=max(ms,ws)
            end=end.next
            head=head.next
        return ms
obj=LinkedList()
head=obj.create()
#obj.display(head)
print(obj.findmaxsum(head,3))