# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if self.preorder(p,[])==self.preorder(q,[]):          
            return True
        else:
            return False
        
    def preorder(self,root,list_):#treeNode类型
        
        if root is None:
            list_.append(None)
            return 
        list_.append(root.val)
        self.preorder(root.left,list_)
        self.preorder(root.right,list_)
        return list_
        
