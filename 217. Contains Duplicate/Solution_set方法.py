class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        else:
            lis=list(set(nums))#set返回的是一个可能与原来list顺序不一样的，无value的字典。
            #lis.sort(key = nums.index)#设置成与原来list相同的顺序的方法，但是这样做会超时。
            return len(lis)!=len(nums)
        
        
        
