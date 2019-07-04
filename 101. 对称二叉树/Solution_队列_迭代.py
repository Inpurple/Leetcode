# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        que=[]
        if not root:
            return True
        else:
            que=[root]
            while que:
                for i in range(len(que)):
                    curnode=que.pop(0)
                    if curnode:
                        que.append(curnode.left)
                        que.append(curnode.right)
                for j in range(0,len(que)/2):
                    if que[j] and que[len(que)-1-j] and  que[j].val==que[len(que)-1-j].val:
                        pass
                    elif que[j]==que[len(que)-1-j]:
                        pass
                    else:
                        return False
                        
            return True
            
