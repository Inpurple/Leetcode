class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        算法：因为额外空间有限制，多一个额外空间用来记录一共有多少个不相同的元素即可   
        Notes：1.unique+1，unique后面的值不需要修改，因为题目的内部设定已经是“根据你的函数返回的长度, 它会打印出数组中该长度  范围内的所有元素”        
        """
        unique=0#用来记录新数组中不同值的下标
        if len(nums)>=2:
            for index in range(1,len(nums)):#index为遍历的索引值，索引值永远是在unique的后面
                if nums[index]!=nums[unique]:#判断遍历的值是否和上一个unique的值相等
                    unique+=1
                    nums[unique]=nums[index]
            return unique+1#一定要注意不是 len(nums)
        else:
            return len(nums)
