# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if not t1:
            return t2
        if not t2:
            return  t1
        t1.val=t1.val+t2.val
        que1=[t1]
        que2=[t2]
        
        while que1:
            curnode1=que1.pop(0)
            curnode2=que2.pop(0)
            if curnode1.left and curnode2.left:
                curnode1.left.val+=curnode2.left.val
                que1.append(curnode1.left)
                que2.append(curnode2.left)
            elif not curnode1.left:
                curnode1.left=curnode2.left
            
            if curnode1.right and curnode2.right:
                curnode1.right.val+=curnode2.right.val
                que1.append(curnode1.right)
                que2.append(curnode2.right)
            elif not curnode1.right:
                curnode1.right=curnode2.right
                
        return t1
 
                
                
                
            
        
