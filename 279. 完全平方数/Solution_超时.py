class Solution:
    def numSquares(self, n: int) -> int:
        
    
        def recur(n,dic):
            i=1
            mi=float('inf')
            if n==0:
                return 0
            if n in dic:
                return dic[n]
            while i**2<=n:
                mi=min(mi,recur(n-i**2,dic)+1)
                i+=1
            dic[n]=mi
            return mi
            
        return recur(n,{})
