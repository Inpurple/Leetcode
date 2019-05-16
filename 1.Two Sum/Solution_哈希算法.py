class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashtable={}
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [i,hashtable[target-num]]
            else:
                hashtable[num]=i
