"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.res=[] 
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        else:
            for child in root.children:
                self.postorder(child)
            self.res.append(root.val)
        return self.res
