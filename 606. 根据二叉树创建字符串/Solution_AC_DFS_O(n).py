# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        def dfs(t):
            if not t:
                return ""
            if not t.right and not t.left:
                return str(t.val)
            elif t.right and t.left:
                return str(t.val)+"("+dfs(t.left)+")"+"("+dfs(t.right)+")"
            elif t.left and not t.right:
                return str(t.val)+"("+dfs(t.left)+")"  
            elif not t.left and t.right:
                return str(t.val)+"()"+"("+dfs(t.right)+")"


        
        return dfs(t)
    
