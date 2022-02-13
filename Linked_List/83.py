# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        curr=head
        ptr=curr.next
        while(ptr):
            if(ptr.val>curr.val):
                curr.next=ptr
                curr=curr.next
            ptr=ptr.next
        curr.next=None
        return head
        