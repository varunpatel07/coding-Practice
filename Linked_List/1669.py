# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if(list1==None):
            return list1
        if(a==0):
            return list2
        start=list1
        end=list1
        a=a-1
        while(a!=0):
            start=start.next
            a-=1

        while(b!=0):
            end=end.next
            b-=1
       
        start.next=list2
        while(start.next!=None):
            start=start.next
        start.next=end.next
        return list1
        