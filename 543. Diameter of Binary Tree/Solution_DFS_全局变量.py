# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res=0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.res
        
    def depth(self,root):#返回此节点的深度
        if not root:
            return 0
        else:
            l=self.depth(root.left)
            r=self.depth(root.right)
            di=l+r
            self.res=max(di,self.res)
            return max(l,r)+1
        
