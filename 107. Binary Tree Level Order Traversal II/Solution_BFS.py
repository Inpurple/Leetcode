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
            return None
        else:
            res=[[root.val]]
            que=[root]
            newque=[root]
            new=[]
            while newque:
                newque=[]
                new=[]
                while que:
                    curnode=que.pop(0)
                    if curnode.left:
                        new.append(curnode.left.val)
                        newque.append(curnode.left)
                    if curnode.right:
                        new.append(curnode.right.val)
                        newque.append(curnode.right)
                que=newque[:]
                if new:
                    res.append(new)
        res.reverse()#返回None
        return res
