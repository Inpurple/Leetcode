class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=[]#最优解的集合
        if not nums:
            return 0#要注意空列表的特殊情况
        
        for i in range(len(nums)):
            if i==0:
                m.append(nums[i])
            elif i==1:
                m.append(max(nums[0],nums[1]))
            else:
                m.append(max(m[i-1],m[i-2]+nums[i]))
                
        return m[len(nums)-1]
