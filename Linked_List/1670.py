class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next= next
class FrontMiddleBackQueue:
    

    def __init__(self):
        self.head=None
        self.length=0
        

    def pushFront(self, val: int) -> None:
        newnode=Node(val)
        if(self.head==None):
            self.head=newnode
            
        else:
            newnode.next=self.head
            self.head=newnode
        self.length+=1
            
        

    def pushMiddle(self, val: int) -> None:
        newnode=Node(val)
        if(self.head==None):
            self.head=newnode
        
        elif(self.length==1):
            self.pushFront(val)
            return
            
        else:
            curr=self.head
            for _ in range((self.length//2)-1):
                curr=curr.next
            newnode.next= curr.next
            curr.next=newnode
        self.length+=1
        

    def pushBack(self, val: int) -> None:
        newnode=Node(val)
        if(self.head==None):
            self.head=newnode
          
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=newnode
        self.length+=1
        

    def popFront(self) -> int:
        if(self.head==None):
            return -1
          
        else:
            val=self.head.val
            self.head=self.head.next
        self.length-=1
        return val
        
    def display(self):
        curr=self.head
        print(f"{self.length}",end=" ")
        while(curr!=None):
            print(curr.val,end=" ")
            curr=curr.next
        print()
        
    def popMiddle(self) -> int:
        self.display()
        if(self.head==None):
            return -1

        if(self.length == 1 or self.length == 2):
            val = self.head.val
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range((self.length-1)//2):
                prev = curr
                curr = curr.next
                
            val=prev.next.val
            prev.next=prev.next.next
        self.length -= 1
        return val
        

    def popBack(self) -> int:
        if(self.head==None):
            return -1
        elif(self.head.next==None):
                val=self.head.val
                self.head=self.head.next
        else:
            curr=self.head
            while(curr.next!=None and curr.next.next!=None):
                curr=curr.next
            val=curr.next.val
            curr.next=None
        self.length-=1
        return val
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()