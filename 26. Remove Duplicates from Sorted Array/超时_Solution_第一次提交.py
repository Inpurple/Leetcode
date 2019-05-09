class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return None
        else:
            count=0
            for index1 in range(0,len(nums)-1):
                for index2 in range(index1+1,len(nums)):
                    if nums[index1]!='s':
                        if nums[index1]==nums[index2]:
                            nums[index2]='s'
                            count+=1
                    else:
                        break
            for i in range(0,count):
                nums.remove('s')
            return len(nums)
