# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count=0
        return self.DFS(root,count)
            
        
    def DFS(self,root,count):
        if not root:
            count+=0
            return count
        else:
            return max(self.DFS(root.left,count+1),self.DFS(root.right,count+1))
