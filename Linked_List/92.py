
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,head,tail):
        nh = None
        nt = head
        while(head!=tail):
            curr = head
            head = head.next
            curr.next = nh
            nh = curr
        if(tail):
            tail.next = nh
            nh = tail
        return (nh,nt)

    def display(self,head):
        while(head!=None):
            print(head.val)
            head=head.next
            
    def reverseBetween(self, head, left: int, right: int):
        if(left==right):
            return head
        start,end = None,None
        curr = head
        #search for left
        if(head.val == left):
            start = head
        else:
            while(curr!=None and curr.next!=None and curr.next.val!=left):
                curr = curr.next
        start = curr

        #search for right
        prev = None
        while(curr!=None and curr.val!=right):
            prev = curr
            curr = curr.next

        if(curr):
            end = curr
        else:
            end = prev
        end_next = end.next
        res = None
        if(start.val == left):
            res = self.reverse(start,end)
            res[1].next = end_next
            return res[0]
        else:
            res = self.reverse(start.next,end)
            start.next = res[0]
            res[1].next = end_next
        

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
obj = Solution()
obj.reverseBetween(head,1,4)
obj.display(head)
