class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        """
        index1=0
        index2=0
        nums1.sort()
        nums2.sort()
        s=[]
        while index1<=len(nums1)-1 and index2<=len(nums2)-1:
            if nums1[index1]<nums2[index2]:
                index1=index1+1
            elif nums1[index1]>nums2[index2]:
                index2=index2+1
            elif nums1[index1]==nums2[index2] and nums1[index1] not in s:
                s.append(nums1[index1])
                index1=index1+1
                index2=index2+1
            #容易漏掉相等并且在收集的集合里的情况而导致死循环
            else:
                index2=index2+1
                index1=index1+1
        return s
                
