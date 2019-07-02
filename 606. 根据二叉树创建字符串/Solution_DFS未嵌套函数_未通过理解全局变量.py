# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res=""
        def dfs(t):
            nonlocal res
            print("RES",res)
            if not t:
                res=res.replace("()","",1)
                print(2,res)
                return 
            elif t:
                if res=="":
                    res=str(t.val)+"()"+"()"
                else: 
                    print(1)
                    res=res.replace("()","("+str(t.val)+"()"+"()"+")",1)
                dfs(t.left)
                dfs(t.right)
        if not t:
            return ""
        else:
            dfs(t)
            return res
    
    
            
                
            
