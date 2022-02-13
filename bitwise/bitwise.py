import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.fn = None
        self.sn = None
        self.prev = TreeNode(-sys.maxsize)
        
    def inOrder(self,root):
        if(root==None):
            return 
        self.inOrder(root.left)
        if(self.fn == None and self.prev.val > root.val):
            self.fn = self.prev
        if(self.fn!=None and self.prev.val > root.val):
            self.sn = root
        self.prev = root
        self.inOrder(root.right)
            
    def recoverTree(self, root) -> None:
        if(root==None):
            return
        
        self.inOrder(root)
        print(self.fn.val)
        print(self.sn.val)
        temp = self.sn.val
        self.sn.val = self.fn.val
        self.fn.val = temp
        
obj = Solution()
r = TreeNode(1)
r.left = TreeNode(3)
r.left.right = TreeNode(2)
obj.recoverTree(r)
        
        