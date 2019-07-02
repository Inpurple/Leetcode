# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        global res
        res=""
        if not t:
            return ""
        else:
            self.dfs(t)
            return res
    
    def dfs(self,t):
        global res
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
            self.dfs(t.left)
            self.dfs(t.right)
 
    
            
                
            
