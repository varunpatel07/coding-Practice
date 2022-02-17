# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if(head==None or head.next==None):
            return head
        curr=head
        temp=head.next
        head.next=head.next.next
        temp.next=head
        head=temp
        while(curr !=None and curr.next!=None and curr.next.next!=None):
            temp=curr.next
            curr.next=temp.next
            temp.next=curr.next.next
            curr.next.next=temp
            curr=curr.next.next     
        return head

    def swapPairs2(self,head):
        if(head==None or head.next==None):
            return head
        prev = None
        curr = head #1|2
        nex = head.next #2|3
        while(curr and curr.next):
            print(curr.val)
            print(nex.val)

            temp = nex.next  #3|4
            nex.next = curr  #2|1
            curr.next = temp  #1|3
            #self.display(head)

            if(prev == None):
                head = nex
            else:
                prev.next = nex

            prev = curr #1|3
            curr = curr.next #3|4
            if(curr):
                nex = curr.next # 4
        return head
        
        
        
    def display(self,head):
        while(head!=None):
            print(head.val,end=" ")
            head=head.next

#[1,2,3,4]
# out = [2,1,4,3]
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
obj = Solution()
obj.display(obj.swapPairs2(head))
print()
