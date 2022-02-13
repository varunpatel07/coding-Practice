import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if(root==None):
            return []
        q=[None,root]
        cmax = -sys.maxsize
        ans=[]
        while(q):
            temp = q.pop()
            if(temp==None):
                if(len(q)!=0):
                    q.insert(0,None)
                ans.append(cmax)
                cmax = -sys.maxsize
            else:
                cmax = max(cmax,temp.val)
                if(temp.left):
                    q.insert(0,temp.left)
                if(temp.right):
                    q.insert(0,temp.right)
        return ans
                