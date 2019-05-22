class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j=0
        r=[]
        while j <=len(nums)-1:
            r.append(-1)
            j+=1
        
        stack=[]
        for i,num in enumerate(nums):
            while stack and num>nums[stack[-1]]:
                r[stack.pop()]=num
            stack.append(i)

        if stack:
            for i,num in enumerate(nums):
                while stack and num>nums[stack[-1]]:
                    r[stack.pop()]=num
                    
        return r
