"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        else:
            res=[]
            que=[root]
            pre=None
            while que:
                curnode=que[0]
                if curnode.children==[] or curnode.children[-1]==pre:#不能写 curnode.children==None
                    #是叶节点或者孩子都访问过了，则出栈
                    res.append(curnode.val)
                    pre=que.pop(0)
                else:
                    for child in curnode.children[::-1]:#逆序遍历
                        que.insert(0,child)
            return res
            
        
        
