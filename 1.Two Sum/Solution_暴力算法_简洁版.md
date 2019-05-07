class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        for index1,element1 in enumerate(nums):
            for index2,element2 in enumerate(nums[index1+1:len(nums)]):
                if element1+element2==target:
                    return [index1,index1+index2+1]
                
