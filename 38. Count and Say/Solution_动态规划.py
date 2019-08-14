class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        dp="1"
        
        for i in range(2,n+1):
            res=""
            count=0

            for j in range(len(dp)):
                
                #变量count计数的情况
                
                if j==0 or dp[j]!=dp[j-1] :#当数字为第一个或者开始换数的时候计数重置为1
                    count=1
                elif dp[j]==dp[j-1]:#当数字和前一数字一样的时候计数加1
                    count+=1
                    
                
                #变量count输出结果的情况，注意与上面if语句会同时满足，并且先计后输出结果
                
                if j==len(dp)-1 or dp[j]!=dp[j+1]:#当数字是最后一个或者和后一个不一样的时候，记下结果
                    res+=str(count)
                    res+=str(dp[j])
                
                    
            dp=res
            print("HELLO",dp)
            
        return dp
            
        
    
