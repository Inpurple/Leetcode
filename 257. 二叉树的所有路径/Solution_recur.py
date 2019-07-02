# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res=[]#python中list变量作为全局变量时，在函数中可以直接修改。而普通变量则需要先在函数中global声明，嵌套函数中要在函数中声明nonlocal，否则会报错。
        temp=""
        def dfs(root,temp):
            temp+=str(root.val)+"->"
            if not root.right and not root.left:
                temp=temp[:-2]
                res.append(temp)
            if root.left:
                dfs(root.left,temp)
            if root.right:
                dfs(root.right,temp)
        if not root:
            return []
        else:
            dfs(root,temp)
            return res
            


            
