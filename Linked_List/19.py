# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        nl=0
        while(curr!=None):
            curr=curr.next
            nl+=1
        
        nodedist=nl-n
        if(nodedist==0):
            head=head.next
            return head
        curr=head
        while(nodedist>1):
            curr=curr.next
            nodedist-=1
        curr.next=curr.next.next
        return head
        