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
        1.凭借中序遍历结果判断是否为对称二叉树是不严谨的！！！
        2.为了规避上面的问题，我们只需在验证中序遍历结果的基础上增加一个判断，那就是验证根节点的左右子节点数值是否相等（前提是左右子节点不为空），如果相等且中序遍历结果对称则必为对称树。
        3.这种方法时间复杂度为O(n),空间复杂度为O(n).
        """
        res=self.inorder(root)
        i=0
        j=len(res)-1
        print(res)
        while i<j:
            if res[i]==res[j]:
                i=i+1
                j=j-1
            else:
                return False
    


        if root and  root.left and root.right and root.left.val!=root.right.val:
                return False
        else:
            return True
            
    def inorder(self,root):
        if not root:
            return [None]
        if not root.left and not root.right:
            return [root.val]
        else:
            return self.inorder(root.left)+[root.val]+self.inorder(root.right)
        
            
            
