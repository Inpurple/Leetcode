class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """算法：
            先替换 ，计算此值的数量，后使用remove
           Notes：
            1.题目描述使用 O(1) 额外空间的条件下，故不能引入新的列表表
            2.更不能直接遍历删除，这样会影响指针。
        """
        count=0
        for index,num in enumerate(nums):
            if num==val:
                count+=1
                nums[index]='a'
        for i in range(count):
            nums.remove('a')
        return len(nums)
