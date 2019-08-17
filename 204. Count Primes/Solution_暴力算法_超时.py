class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n==1 or n==0 or n==2:
            return 0

        lis=[]
        i=2
        while i<n:
            flag=0
            for di in lis :
                if i%di ==0 and i/di!=1:
                    flag=1
                    break
            if flag==0:
                lis.append(i)
            i+=1
        return len(lis)
