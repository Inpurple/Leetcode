class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        

        
        
        def recur(small,big):
            if abs(small-big)==1:
                return small
            mid=(small+big)//2
            if mid**2==x:
                return mid
            if mid**2>x:
                return recur(small,mid)
            else:
                return recur(mid,big)
            
        if x==1:#预感只有这一个特殊情况！
            return 1
        return recur(0,x)
