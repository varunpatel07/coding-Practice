# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates2(self, head):
        if(head==None):
            return None
        flg = False
        while(head.next and head.next.val==head.val):
            head = head.next
            flg = True
        if(head):
            head.next = self.deleteDuplicates(head.next)
        return head.next if flg else head

    #sentinal approach
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        curr = dummy
        while(head):
            isskipped = True
            while(head.next and head.val == head.next.val):
                isskipped = False
                head= head.next
            if(isskipped):
                curr.next = head
                curr = curr.next
            head = head.next
        curr.next = None
        return dummy.next
    def display(self,head):
        while(head!=None):
            print(head.val,end=" ")
            head=head.next
"""
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(2)
obj = Solution()
print(obj.display(obj.deleteDuplicates(head)))