# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        elif root.left and root.left.val!=root.val:
            return False
        elif root.right and root.right.val!=root.val:
            return False
        else:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
