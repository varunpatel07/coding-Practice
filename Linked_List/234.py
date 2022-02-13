# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLen(self, curr1: ListNode) -> int:
        lenA = 0
        while(curr1!=None):
            lenA+=1
            curr1=curr1.next
        return lenA
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        
        for i in range(lenA - lenB):
            headA = headA.next

        for i in range(lenB - lenA):
                headB = headB.next

        while(headA != headB):
            headA = headA.next
            headB = headB.next
        return headA