# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res=[]
        self.recur(root,0)
        return self.res
        
    def recur(self,root,i):
        if not root:
            return
        if i>len(self.res)-1:
            self.res.append([])
        self.res[i].append(root.val)
        
        self.recur(root.left,i+1)
        self.recur(root.right,i+1)
    
