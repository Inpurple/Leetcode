class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb(n,{})
        
        
    def climb(self,n,dic):
        if n==1:
            return 1
        if n==2:
            return 2
        if n in dic:
            return dic[n]
        else:
            dic[n]=self.climb(n-1,dic)+self.climb(n-2,dic)
            return dic[n]
            
