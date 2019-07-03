# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(root,temp):
            nonlocal sum
            temp=temp+str(root.val)
            if not root.left and not root.right:
                sum+=int(temp,2)
                return 
            if root.left:
                preorder(root.left,temp)
            if root.right:
                preorder(root.right,temp)
                
        res=[]
        if not root:
            return 0
        else:
            sum=0
            preorder(root,'')
            return sum
