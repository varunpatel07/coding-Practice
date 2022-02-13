# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nh=None
        while(head!=None):
            curr=head
            head=head.next
            curr.next=nh
            nh=curr
        i=0
        s=0
        while(nh!=None):
            s+=nh.val*(2**i)
            nh=nh.next
            i+=1
        return s
        