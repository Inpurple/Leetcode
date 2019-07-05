# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.recur(root.left,root.right)
        
        
    def recur(self,t1,t2):
        """
        思路：要带入两个节点，返回两个树是否对称
        """
        if t1==t2==None:
            return True
        elif t1 and t2:
            return t1.val==t2.val and self.recur(t1.left,t2.right) and self.recur(t1.right,t2.left)
        else:
            return False
