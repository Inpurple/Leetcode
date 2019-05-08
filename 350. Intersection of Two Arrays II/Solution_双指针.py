class Solution(object):
    def intersect(self, nums1, nums2):
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
            elif nums1[index1]==nums2[index2]:
                s.append(nums1[index1])
                index1=index1+1
                index2=index2+1

        return s
