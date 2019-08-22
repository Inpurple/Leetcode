# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        1.关键是判断最近公共祖先的逻辑:如果在遍历的任何点上，左、右或中三个标志中的任意两个变为 true，这意味着我们找到了节点 p 和 q 的最近公共祖先。
        2.注意参数和返回值的数据类型。
        """
        self.res = None
        self.dfs(root,p,q,0)
        return self.res
        
        
        
    def dfs(self,root,p,q,mid):
        if not root:
            return 0
        mid = root == p or root == q #不能用if语句代替，一定要保证mid有，可以不传递参数mid。
        left=self.dfs(root.left,p,q,mid)
        right=self.dfs(root.right,p,q,mid)
        
        if left+right+mid>1:
            self.res=root
        return mid or left or right  #无需写 某种情况下 return 1 的情况
        
      
      
