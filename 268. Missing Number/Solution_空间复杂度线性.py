class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(1)---常数
        """
        lis=["" for x in range(0, len(nums)+1)]#列表生成式
        for i in range(0,len(nums)):
            lis[nums[i]]=nums[i]
        
        return lis.index("")#lis的通过元素找索引的方法
