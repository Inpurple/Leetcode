class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        常见错误：
        1.读取切片的值会浅拷贝占用额外的内存空间。应该用一个整形变量计数即可。
        2.如果用for迭代索引，同时删除被迭代的数组，会造成错误
        3.审题未注意有序数列
        """
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                k=k+1#有k个不相同的
                nums[k-1]=nums[i]#很巧妙的方法前面是不相同的数列，避开了改变数组
                
        return k
            
