"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head==None):
            return None
        #to store all the ne copies of list
        store = {}
        
        oldCurr = head
        newHead = Node(oldCurr.val)
        store[head] = newHead
        oldCurr =  oldCurr.next
        newCurr = newHead
        
        while(oldCurr):
            newCurr.next = Node(oldCurr.val)
            store[oldCurr] = newCurr.next
            oldCurr = oldCurr.next
            newCurr = newCurr.next
        
        oldCurr = head
        newCurr = newHead
        while(oldCurr):
            newCurr.random = store[oldCurr.random] if oldCurr.random else None 
            newCurr = newCurr.next
            oldCurr = oldCurr.next
        return newHead
        
        
            
        
        
        