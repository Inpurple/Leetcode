class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        当一个算法的空间复杂度为一个常量，即不随被处理数据量n的大小而改变时，可表示为O(1)
        """
        count=0
        same=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and same <2 :
                count=count+1
                same=same+1
                nums[count]=nums[i]
            elif nums[i]==nums[i-1] and same>=2:
                pass
            elif nums[i]!=nums[i-1]:
                same=1
                count=count+1
                nums[count]=nums[i]
        return count+1#返回长度即可
