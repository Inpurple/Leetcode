"""Bottom-up 提前阻断法（复杂度 O(N)）

在对root做dfs时，会从下至上获得每个root的左右子树高度，当我们发现有一例左右子树高度差 ＞1的情况时return -1，代表此树不是平衡树，后面的高度计算都没有意义了，之后一路return -1，不再做后面的DFS。

PythonJavaclass Solution:
"""
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left,right) + 1 if abs(left - right) < 2 else -1
