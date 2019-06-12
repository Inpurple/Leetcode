class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]#后面代码的循环中，找到某一个index值的时间复杂度为O（1）
            #必须给index为0的值赋值，否则将出现，list index out of range
                
            
        for i in range(1,n+1):
            if i==1:
                dp.insert(i,1)
            elif i==2:
                dp.insert(i,2)
            else:
                dp.insert(i,dp[i-1]+dp[i-2])
                
        return dp[n]
        
