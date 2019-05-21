class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r={}
        stack=[]
        
        for num in nums2:
            while stack and num>stack[-1]:
                r[stack.pop()]=num
            stack.append(num)
            #只有满足条件（后面的列表有第一个比num大的值）字典才有对应的键值
            
        return[r.get(i,-1) for i in nums1]#如果字典找不到i,则返回"-1"
