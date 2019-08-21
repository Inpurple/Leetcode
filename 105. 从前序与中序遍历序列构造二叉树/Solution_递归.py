# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head=TreeNode(preorder[0])
        self.recur(preorder,inorder,head)#此处head不需要变成self.head
        return head
        
    def recur(self,preorder: List[int], inorder: List[int],treenode):
        """
        #非常重要的创建二叉树的步骤。
        1.不能treenode.left.val=TreeNode(leftarray[0])。
        因为treenode.left.为空，没有此数据属性
        2.也不能以treenode.left为空传递到下一个递归中，再赋值为一个节点的类。这样会导致树没有接上。
            
        """
        if not inorder:
            treenode=None
            return
        i=inorder.index(preorder[0])
        
        leftarray=preorder[1:1+i]
        if leftarray:
            treenode.left=TreeNode(leftarray[0])#非常重要的创建二叉树的步骤。
            self.recur(leftarray,inorder[0:i],treenode.left)
            
        rightarray=preorder[1+i:len(preorder)]
        if rightarray:
            treenode.right=TreeNode(rightarray[0])#非常重要的创建二叉树的步骤。
            self.recur(rightarray,inorder[i+1:len(preorder)],treenode.right)
            
            
        
        
