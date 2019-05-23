class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)#O(n)
        nums=list(nums_set)
        if len(nums)==3:
            return min(nums)
        elif len(nums)<3:
            return max(nums)
        else:
            nums.remove(max(nums))#O(n)
            nums.remove(max(nums))#O(n)
            return max(nums)
