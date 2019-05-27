class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dq=[]#最优解的集合
        if nums:
            for n in range(0,len(nums)):
                if n==0:
                    dq.insert(0,nums[0])
                elif n==1:
                    dq.insert(1,max(nums[0],nums[1]))
                else:
                    dq.insert(n,max(nums[n]+dq[n-2],dq[n-1]))
                print(dq)
            return dq[len(nums)-1]
        else:
            return 0
        
