# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res=[]
        self.recur(root,res,k)#如果要是变量在函数中发生改变，1.传递可变类型，2.传递数据属性。3.将变量设为全局变量
        return res[-1]
        
    def recur(self,root,res,k):
        if not root:
            return
        if len(res)==k:
            return 
        self.recur(root.left,res,k)
        if len(res)<k:
            res.append(root.val)
        self.recur(root.right,res,k)
