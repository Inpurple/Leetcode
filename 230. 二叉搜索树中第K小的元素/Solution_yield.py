class Solution:
    def mid_order(self, root):
        if not root: return
        yield from self.mid_order(root.left)
        yield root.val
        yield from self.mid_order(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        gen = self.mid_order(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)
