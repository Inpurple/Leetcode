class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp=[]
        for i in range(0,N+1):
            if i==0:
                dp.insert(i,0)
            elif i==1:
                dp.insert(i,1)
            else:
                dp.insert(i,dp[i-1]+dp[i-2])
                
        return dp[N]
