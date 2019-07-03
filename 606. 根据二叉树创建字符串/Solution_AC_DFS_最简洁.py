# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        if not t:
            return ""
        else:
            left="("+self.tree2str(t.left)+")"if t.left or t.right else ""
            right="("+self.tree2str(t.right)+")"if t.right else ""
            return str(t.val)+left+right
        
        
