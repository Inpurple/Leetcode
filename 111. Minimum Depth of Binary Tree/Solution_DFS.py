    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count=0

        return self.DFS(root,count)
            
        
    def DFS(self,root,count):
        if not root.right and not root.left:
            return count
        elif root.left and root.right:
            return min(self.DFS(root.left,count+1),self.DFS(root.right,count+1))
        elif not root.left and root.right:
            return self.DFS(root.right,count+1)
        elif not root.right and root.left:
            return self.DFS(root.left,count+1)
