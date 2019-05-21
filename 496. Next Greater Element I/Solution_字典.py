class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        并没有提高效率
        """
        r={}
        if nums2:
            r[nums2[-1]]=-1 #nums2的末尾，绝对不会有比它大的值,注意要排除空的情况
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    r[nums2[i]]=nums2[j]
                    break
                if j==len(nums2)-1:#最后一个都没有找到比它大的值
                    r[nums2[i]]=-1
                
        return [r.get(i) for i in nums1]
