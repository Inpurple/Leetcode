# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def recur(root,k):
            if not root:
                return 0
            if not root.right and not root.left and k==1:
                return root.val
            if not root.right and not root.left and k==0:
                return 0

            else:
                return recur(root.left,1)+recur(root.right,0)
        return recur(root,0)
        
