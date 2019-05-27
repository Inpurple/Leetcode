class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0#要注意空列表的特殊情况
        odd=0
        for i in range(len(nums)):
            if i==0:
                even=nums[i]
            elif i==1:
                odd=max(nums[0],nums[1])
            elif i%2==0:
                even=max(even+nums[i],odd)
            else:
                odd=max(odd+nums[i],even)

                
        return max(even,odd)
