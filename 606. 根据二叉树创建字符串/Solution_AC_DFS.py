# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    执行结果：通过
    显示详情 
    执行用时 :436 ms, 在所有 Python3 提交中击败了6.94%的用户
    内存消耗 :15.7 MB, 在所有 Python3 提交中击败了41.67%的用户
    """
    def tree2str(self, t: TreeNode) -> str:
        res="()"# 这样做在子函数中就不用考虑特殊情况了，在结尾删除即可
        def dfs(t):
            nonlocal res
            if not t.right and not t.left:
                res=res.replace("()","("+str(t.val)+")",1) 
                return
            elif t.right and t.left:
                res=res.replace("()","("+str(t.val)+"()"+"()"+")",1)  
                dfs(t.left)
                dfs(t.right)
            elif t.left and not t.right:
                res=res.replace("()","("+str(t.val)+"()"+")",1)    
                dfs(t.left)
            elif not t.left and t.right:
                res=res.replace("()","("+str(t.val)+"(N)"+"()"+")",1) 
                dfs(t.right)
        if not t:
            return ""
        else:
            dfs(t)
            res=res.replace("(N)","()")
        
            return res[1:-1]
    
    
            
                
            
