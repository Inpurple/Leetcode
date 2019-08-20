class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1]*len(nums)
        
        xpre=1
        for i in range(len(nums)):
            res[i]=xpre
            xpre=xpre*nums[i]
            
        xafter=1
        for j in range(-1,-len(nums)-1,-1):#而不是(-1:-1:-1)
            res[j]=res[j]*xafter
            xafter=xafter*nums[j]
            
        return res
