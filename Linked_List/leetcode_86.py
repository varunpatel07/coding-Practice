# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        nh,nt=None,None
        if(head==None):
            return head
        
        if(head.val<x):
            nh=nt=head
        while(head!=None and head.val<x ):
            nt=head
            head=head.next
        curr=head
        while(curr!=None and curr.next!=None):
            
            if(curr.next.val<x):
                if(nh==None):
                    nh=nt=curr.next
                else:
                    nt.next=curr.next
                    nt=nt.next
                curr.next=curr.next.next
            else:
                curr=curr.next
        if(nh!=None):
            nt.next=head
            return nh
        else:
            return head
    def display(self,head):
        while(head!=None):
            print(head.val,end=" ")
            head=head.next

#[5,-5,0,-8,3,8,-8,0,-1,3,-8,7,-4,-8,2,5,9,4,-5,-6]
head=ListNode(5)
head.next=ListNode(-5)
head.next.next=ListNode(0)
head.next.next.next=ListNode(-8)
head.next.next.next.next=ListNode(3)
head.next.next.next.next.next=ListNode(8)
head.next.next.next.next.next.next=ListNode(-8)
head.next.next.next.next.next.next.next=ListNode(0)
head.next.next.next.next.next.next.next.next=ListNode(-1)
head.next.next.next.next.next.next.next.next.next=ListNode(3)
head.next.next.next.next.next.next.next.next.next.next=ListNode(-8)
head.next.next.next.next.next.next.next.next.next.next.next=ListNode(7)
head.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(-4)
head.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(-8)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(2)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(5)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(9)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(4)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(-5)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next=ListNode(-6)
obj=Solution()
obj.display(obj.partition(head,-4))