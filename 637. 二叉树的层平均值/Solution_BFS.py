# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        else:
            res=[]
            que=[root]
            while que:
                temp=0
                n=len(que)
                for i in range(n):
                    curnode=que.pop(0)
                    temp+=curnode.val
                    if curnode.left:
                        que.append(curnode.left)
                    if curnode.right:
                        que.append(curnode.right)
                
                res.append(temp/float(n))#py3直接除以整数就是除法，py2需要把除数列为浮点型。
        return res
                    
                    
        
