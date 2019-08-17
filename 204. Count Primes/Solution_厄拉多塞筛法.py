class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        res=0
        isPrime=[1]*n
        
        for i in range(2,n):
            if isPrime[i]==1:
                res+=1
                j=i
                while j*i<n:
                    isPrime[j*i]=0
                    j+=1
        return res
        
            
