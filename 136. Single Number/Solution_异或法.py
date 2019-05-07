class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。
        """
        
        res = 0
        for i in nums:
            res^=i
        return res
