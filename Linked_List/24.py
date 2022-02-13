# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        
        
        
        