# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #this can be solved using stack because we are popping element in last in first out         manner
        if(head==None or k==0):
            return head
        end=head
        llen=1
        while(end.next!=None):
            llen+=1
            end=end.next
        newk=k%llen
        llen=llen-newk
        if(newk==0):
            return head
    
        start=head
        while(llen!=1):
            start=start.next
            llen-=1
        
        temp=head
        head=start.next
        start.next=None
        end.next=temp
        return head
        
        