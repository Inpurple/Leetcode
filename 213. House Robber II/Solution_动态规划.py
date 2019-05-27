class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=[]
        n=[0]
        if not nums :
            return 0#要注意空列表的特殊情况
        if len(nums)==1:
            return nums[0]
        
        for i in range(len(nums)-1):
            if i==0:
                m.append(nums[i])
            elif i==1:
                m.append(max(nums[0],nums[1]))
            else:
                m.append(max(m[i-1],m[i-2]+nums[i]))
                
        for i in range(1,len(nums)):
            if i==1:
                n.append(nums[i])
            elif i==2:
                n.append(max(nums[2],nums[1]))
            else:
                n.append(max(n[i-1],n[i-2]+nums[i]))
                
        return max(m[len(nums)-2],n[len(nums)-1])
