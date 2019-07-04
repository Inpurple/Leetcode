# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root:
            NodeTilt=abs(self.sumNode(root.left) - self.sumNode(root.right))
            return NodeTilt+self.findTilt(root.left)+self.findTilt(root.right)
        
    def sumNode(self,root):
        if not root:
            return 0
        else:
            return root.val+self.sumNode(root.left)+self.sumNode(root.right)
