class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        s=0
        self.array={}
        for k in range(0,len(nums)):
            s=s+nums[k]
            self.array[k]=s#只算一次，题目有说There are many calls to sumRange function.
            
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
    

        if i>=1:
            return self.array[j]-self.array[i-1]
        else:
            return self.array[j]
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
