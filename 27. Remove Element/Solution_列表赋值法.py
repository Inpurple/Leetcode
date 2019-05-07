class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0#计数的变量，即方便输出，又不用删除列表的元素方便迭代
        
        for num in nums:
            if num!=val:
                nums[k]=num
                k=k+1
                
        return k 
