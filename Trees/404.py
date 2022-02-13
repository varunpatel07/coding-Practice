#sol 1 using instance Variable
class Solution:
    def __init__(self):
        self.ans=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        if(root.left and root.left.left==None and root.left.right==None):
            self.ans+=root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.ans

#sol2 using argumment
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        return self.helper(root,'')
    
    def helper(self,root,pos):
        if(root==None):
            return 0
        
        if(root.left==None and root.right==None and pos=='L'):
            return root.val
        
        return self.helper(root.left,'L')+self.helper(root.right,'R')
        
        