"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:

        
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        else:
            res=[]
            que=[root]
            pre=None
            while que:
                curnode=que.pop(0)
                res.append(curnode.val)
                if curnode.children:
                    for child in curnode.children[::-1]:#逆序遍历
                        que.insert(0,child)
            return res
            
        
        

