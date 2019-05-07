class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_=nums[0]
        s=0
        for num in nums:
            if s<0:
                s=num
            else:
                s=num+s#非常巧妙的动态规划的方法
            max_=max(s,max_)
            print(max_)
        return max_
