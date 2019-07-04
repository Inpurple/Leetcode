# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
