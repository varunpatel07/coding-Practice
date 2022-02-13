# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr=[]
        self.soln(root,"",arr)
        return arr
        
        
    def soln(self,root,val,ans):
        if(root == None):
            return
        val+=str(root.val)
        if(root.left==None and root.right==None):
            ans.append(val)
            return
        val+="->"
        if(root.left):
            self.soln(root.left,val,ans)
        if(root.right):
            self.soln(root.right,val,ans)
        

        