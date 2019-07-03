# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def sumRootToLeaf(self, root: TreeNode) -> int:
            
            def preorder(root,num):
                if not root:
                    return 0
                else:
                    num=num*2+root.val
                    if not root.left and not root .right:
                        return num
                    else:
                        return preorder(root.left,num)+preorder(root.right,num)
                    
            return preorder(root,0)
        
