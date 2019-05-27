class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        
        return max(self.rob_line(nums[1:len(nums)]),self.rob_line(nums[0:len(nums)-1]))
        
        
        
    def rob_line(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0#要注意空列表的特殊情况
        if len(nums)==1:
            return nums[0]
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
