# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.trans(root1)==self.trans(root2)
        
    def trans(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            return self.trans(root.left)+self.trans(root.right)
