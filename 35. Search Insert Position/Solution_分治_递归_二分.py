class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.recur(0,len(nums)-1,nums,target)
        
        
        
    def recur(self,left,right,nums,target):
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if left==right:
            if target<nums[left]:
                return left
            elif target>nums[left]:
                return left+1
        elif nums[mid]<target:
            return self.recur(mid+1,right,nums,target)#如果没有return 会返回空值
        elif nums[mid]>target:
            return self.recur(left,mid,nums,target)#要将mid包括进去。因为如果输入是[1,3]，target=0，会无穷尽的递归
