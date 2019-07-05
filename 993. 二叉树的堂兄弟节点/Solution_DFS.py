# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x=x
        self.y=y
        self.res=[]

        self.dfs(root,0)
        if len(self.res)==2 and self.res[0][1]!=self.res[1][1] and self.res[0][2]==self.res[1][2]:
            return True
        else:
            return False
            
    def dfs(self,root,depth):
        if not root:
            return 
        if not root.left and not root.right:
            return 
        else:
            if root.left and root.left.val==self.x:
                self.res.append([root.left.val,root.val,depth])
            elif root.right and root.right.val==self.x:
                self.res.append([root.right.val,root.val,depth])
            
            if root.left and root.left.val==self.y:
                self.res.append([root.left.val,root.val,depth])
            elif root.right and root.right.val==self.y:
                self.res.append([root.right.val,root.val,depth])
                
            self.dfs(root.left,depth+1)
            self.dfs(root.right,depth+1)
