# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        :type nums: List[int]
        :rtype: TreeNode
        二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 
        若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
        若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
        """

        if not nums:
            return
        if len(nums)==1:
            return TreeNode(nums[0])
        else:
            m=len(nums)//2
            cur=TreeNode(nums[m])
            cur.left=self.sortedArrayToBST(nums[0:m])
            cur.right=self.sortedArrayToBST(nums[m+1:len(nums)])
            return cur
