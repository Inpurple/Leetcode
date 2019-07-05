# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        que=[]
        if not root:
            return -1
        else:
            que=[root]
            rootv=root.val
            res=[]
            while que:
                curnode=que.pop(0)
                if curnode.left:
                    que.append(curnode.left)
                    if curnode.left.val>rootv:
                        res.append(curnode.left.val)
                if curnode.right:
                    que.append(curnode.right)
                    if curnode.right.val>rootv:
                        res.append(curnode.right.val)
                        
            if res:
                return min(res)
            else:
                return -1
