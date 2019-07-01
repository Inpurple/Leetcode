# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            res=[]
            que=[root]
            while que:
                temp=[]
                n=len(que)
                for i in range(n):
                    curnode=que.pop(0)
                    temp.append(curnode.val)
                    if curnode.left:
                        que.append(curnode.left)
                    if curnode.right:
                        que.append(curnode.right)

                res.insert(0,temp)
        return res
                    
                    
        
