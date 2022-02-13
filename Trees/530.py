import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        self.mind = sys.maxsize
    def getMinimumDifference(self, root) -> int:
        if(root==None):
            return

        self.getMinimumDifference(root.left)
        
        if(self.prev!=None):
            self.mind = min(self.mind,abs(self.prev - root.val))
        self.prev = root.val
        self.getMinimumDifference(root.right)
        return self.mind

    def inOrder(self,root):
        if(root == None):
            return
        self.inOrder(root.left)
        print(root.val,end = " ")
        self.inOrder(root.right)
#[0,null,2236,1277,2776,519]
root = TreeNode(0)
root.right = TreeNode(2236)
root.right.left= TreeNode(1277)
root.right.right= TreeNode(2776)
root.right.left.left= TreeNode(519)

obj = Solution()
print(obj.getMinimumDifference(root))
obj.inOrder(root)
        