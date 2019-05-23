class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 0
        l = sorted(list(d.keys()))
        if len(l) < 3:
            return max(l)
        return l[-3]
        
            
