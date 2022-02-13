# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity is O(n^2) as depth function is called for everyode 
class Solution:
    def depth(self,root):
        if(root==None):
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1

    def isBalanced(self, root) -> bool:
        if(root==None):
            return True
        if(abs(self.depth(root.left)-self.depth(root.right))>1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# O(N)
class Solution2:
    def isBalanced(self, root) -> bool:
        
        def helper(root):
            if(root == None):
                return 0
            
            left = helper(root.left)
            if(left==-1):
                return -1
            right = helper(root.right)
            if(right==-1):
                return -1
            if(abs(left-right)>1):
                return -1
            return max(left,right)+1
        return helper(root)!=-1
            
        
                
        
        
            
        
        