# minimum depth of binary tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
         if root == None:
            return 0 
         lh = self.minDepth(root.left)
         rh = self.minDepth(root.right)
         if root.left == None or root.right == None:
            return 1+max(lh,rh)
         else:
            return 1+min(lh,rh)

        
