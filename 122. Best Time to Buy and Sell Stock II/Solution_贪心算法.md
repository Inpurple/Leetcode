class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s=0
        for cur in range(len(prices)):
            if cur>0 and prices[cur]>prices[cur-1]:
                p=prices[cur]-prices[cur-1]
                s=p+s
        return s
