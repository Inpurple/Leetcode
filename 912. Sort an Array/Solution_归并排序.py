class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.recur(0,len(nums)-1,nums)
        return nums
        
        
        
    def merge(self,left,right,mid,nums):
        i=left
        j=mid+1
        temp=[]
        while i<=mid and j<=right:
            if nums[i]<nums[j]:
                temp.append(nums[i])
                i=i+1
            else:
                temp.append(nums[j])
                j=j+1
        while i<=mid:
                temp.append(nums[i])
                i=i+1
        while j<=right:
                temp.append(nums[j])
                j=j+1

        for k in range(len(temp)):
            nums[left+k]=temp[k]
            
        
    def recur(self,left,right,nums):
        if left>=right:
            return
        mid=(left+right)//2
        self.recur(left,mid,nums)
        self.recur(mid+1,right,nums)
        self.merge(left,right,mid,nums)
