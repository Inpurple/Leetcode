class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i <=len(nums)-1:#观察如果用for迭代nums的索引，是否会造成错误
            if nums[i] in nums[:i]:
                del(nums[i])
            else:
                i=i+1
        return len(nums)
