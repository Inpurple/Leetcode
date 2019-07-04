# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res=True#使用类的数据属性可以避免子函数对此数据修改前，需要声明全局变量
        def recur(root):
            #返回每个数的高度
            if not root:
                return 0
            dl=recur(root.left)
            dr=recur(root.right)
            if abs(dl-dr)>1:
                self.res=False
            if root:
                return max(dl,dr)+1
        recur(root)
        return self.res

                
