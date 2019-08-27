class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n=len(nums)
        
        def dfs(i,temp):
            res.append(temp)
            if i>=n:#其实不需要，range(i,n)可自动检测 
                return
            
            for j in range(i,n):#不要忘记range,如果忘记range则是遍历一个元祖
                dfs(j+1,[nums[j]]+temp)
                
        dfs(0,[])
        return res
