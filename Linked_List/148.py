"""
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""
from heapq import  heapify,heappop,heappush
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if(head==None or head.next==None):
            return head
        heap = [] 
        curr = head
        while(curr):
            heap.append((curr.val,id(curr),curr))
            curr = curr.next
        heapify(heap)
        nh = curr = None
        while(heap):
            val,i,obj = heappop(heap)
            obj.next = None
            if(nh==None):
                nh = curr = obj
            else:
                curr.next = obj
                curr = obj
        return nh
        
    
    def display(self,head):
        while(head):
            print(head.val)
            head=head.next

#[4,19,14,5,-3,1,8,5,11,15]
head=ListNode(4)
head.next=ListNode(9)
head.next.next=ListNode(14)
head.next.next.next=ListNode(5)
head.next.next.next.next=ListNode(-3)
head.next.next.next.next.next=ListNode(8)
head.next.next.next.next.next.next=ListNode(5)

obj = Solution()
obj.display(obj.sortList(head))