class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''粗暴方法,O(n的平方)超出时间限制
        diff=0
        dic={}
        for index2 in range(0,len(prices)):
            for index1 in range(0,len(prices)):
                if index2>index1:
                    diff=max(prices[index2]-prices[index1],diff)
        if diff>0:
            return diff
        else:
            return 0
        '''
        """动态规划：每一次遍历可以去记录到遍历的那个元素为止，最小值。
                    最后目的一定是，每次遍历一定是遍历的这个值减去那个那个最小值
        """
        diff=0
        if prices:
            min_p=prices[0]
            for price in prices:
                min_p=min(price,min_p)
                diff=max(diff,price-min_p)
            return diff
        if diff>0:
            return diff
        else:
            return 0
