class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        """
        left=0
        right=len(nums)-1
        while left<=right:#包括了单列表的情景，无须考虑列表的长度为基数或者偶数。
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        return -1
