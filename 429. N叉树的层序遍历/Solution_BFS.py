"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        else:
            res=[]
            que=[root]
            while que:
                temp=[]
                for i in range(len(que)):
                    curnode=que.pop(0)
                    temp.append(curnode.val)
                    for child in curnode.children:
                        que.append(child)
                res.append(temp)
            return res
                        
            
            
