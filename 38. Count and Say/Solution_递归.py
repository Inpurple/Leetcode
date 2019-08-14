class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        
        last=self.countAndSay(n-1)

        count=0
        res=""
        
        
        for j in range(len(last)):

            #变量count计数的情况

            if j==0 or last[j]!=last[j-1] :#当数字为第一个或者开始换数的时候计数重置为1
                count=1
            elif last[j]==last[j-1]:#当数字和前一数字一样的时候计数加1
                count+=1


            #变量count输出结果的情况，注意与上面if语句会同时满足，并且先计后输出结果

            if j==len(last)-1 or last[j]!=last[j+1]:#当数字是最后一个或者和后一个不一样的时候，记下结果
                res+=str(count)
                res+=str(last[j])
                
        return res
        
