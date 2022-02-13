# Definition for singly-linked list.
from heapq import heappop, heappush,heapify
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        heap = []

        chead,mhead = None,None
        for i in range(len(lists)):
            if(lists[i]!=None):
                heap.append((lists[i].val,i))
        heapify(heap)

        while(heap):
            #print(heap)
            val,idx = heappop(heap)
            if(mhead == None):
                mhead =chead = lists[idx]
            else:
                chead.next = lists[idx]
                chead = chead.next
            lists[idx] = lists[idx].next
            if(lists[idx]!=None):
                heappush(heap,(lists[idx].val,idx))
            chead.next = None
        return mhead
            

        

    def display(self,root):
        while(root!=None):
            print(root.val)
            root = root.next

obj = Solution()
r1 = ListNode(1,ListNode(4,ListNode(5)))
r2 = ListNode(1,ListNode(3,ListNode(4)))
r3 = ListNode(2,ListNode(6))
inp = [r1,r2,r3]
#print(obj.mergeKLists(inp))
obj.display(obj.mergeKLists([]))
