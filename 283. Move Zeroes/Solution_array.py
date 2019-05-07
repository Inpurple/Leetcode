class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        将数组理解为零集团+数字,zero为零集团的首位，往后遍历的数字如果不是0，和zero互换值，如果是0，继续遍历
        
        """
        zero=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero=zero+1
        return nums
