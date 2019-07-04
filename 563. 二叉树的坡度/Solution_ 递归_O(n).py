# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.treetilt = 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumNode(root)
        return self.treetilt
        
    def sumNode(self,root):
        if not root:
            return 0
        else:
            left=self.sumNode(root.left)
            right=self.sumNode(root.right)
            nodetilt=abs(left - right)
            self.treetilt+=nodetilt
            return root.val+left+right
        
"""
以上复杂度为O（n）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.treetilt = 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumNode(root)
        return self.treetilt
        
    def sumNode(self,root):
        if not root:
            return 0
        else:
            nodetilt=abs(self.sumNode(root.left) - self.sumNode(root.right))
            self.treetilt+=nodetilt
            return root.val+self.sumNode(root.left)+self.sumNode(root.right)

这样写思路正确，但会多次进入递归，使self.treetilt变大。

"""
