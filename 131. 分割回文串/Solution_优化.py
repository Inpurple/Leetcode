class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        
        def dfs(ny,recured):
            if not ny:
                res.append(recured)
                return
            for i in range(1,len(ny)+1):#分隔的技巧写法
                if ny[:i]==ny[:i][::-1]:#回文串的技巧写法
                    dfs(ny[i:],recured+[ny[:i]])
            
                    
        dfs(s,[])
        return res
