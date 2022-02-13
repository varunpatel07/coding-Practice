# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nh,nt=None,None
        if(head==None):
            return head
        
        if(head.val<x):
            nh=nt=head
        while(head!=None and head.val<x ):
            nt=head
            head=head.next
        curr=head
        
        while(curr!=None and curr.next!=None):
            if(curr.next.val<x):
                if(nh==None):
                    nh=nt=curr.next
                else:
                    nt.next=curr.next
                    nt=nt.next
                curr.next=curr.next.next
            else:
                curr=curr.next
        if(nh!=None):
            nt.next=head
            return nh
        else:
            return head
        