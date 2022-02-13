# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None):
            return None
        lenA=0
        nk=k
        curr=head
        endk=head
        startk=None
        while(curr!=None):
            if(nk!=0):
                startk=curr
                nk-=1
            lenA+=1
            curr=curr.next
        for i in range(lenA-k):
            endk=endk.next
        startk.val,endk.val=endk.val,startk.val
        return head
        
        
        