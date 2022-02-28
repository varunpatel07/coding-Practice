"""
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""
from heapq import  heapify,heappop,heappush
from socket import SO_RCVLOWAT
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
# Merge sort approch takes NlogN time with constant space
#     
    def sortListS(self,head):
    
        if(head==None or head.next==None):
            return head
        temp = head
        slow = head
        fast = head
        while(fast and fast.next):
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        left = self.sortListS(head)
        right = self.sortListS(slow)
        return self.merge(left,right)

    def merge(self,left,right):
        nh = None
        curr = None
        while(left and right):
            val  = None
            if(left.val<right.val):
                val = left
                left = left.next
            else:
                val = right
                right = right.next
            val.next==None

            if(nh==None):
                nh = curr = val
            else:
                curr.next = val
                curr = curr.next
        if(left):
            curr.next = left
        if(right):
            curr.next = right
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
obj.display(obj.sortListS(head))