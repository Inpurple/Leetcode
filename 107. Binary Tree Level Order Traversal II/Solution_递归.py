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
        res=[]
        def recur(root,depth):
            if not root:
                return 
            else:
                if depth==len(res):
                    
                    res.insert(0,[])
                res[-(depth+1)].append(root.val)
                #res[0].append(root.val)这样写会有bug，因为在append3的时候，res已经为([[4, 5], [2], [1]], 1, 3)
                recur(root.left,depth+1)
                recur(root.right,depth+1)
        recur(root,0)
        return res
        
