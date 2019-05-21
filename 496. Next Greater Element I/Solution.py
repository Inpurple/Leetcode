class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        AC 64 ms	11.9 MB
        """
        r=[]
        
        for i in range(len(nums1)):
            flag=0
            i2=nums2.index(nums1[i])
            print(i2)
            if i2==len(nums2)-1:
                r.append(-1)
                continue
            for j in range(i2+1,len(nums2)):
                if nums2[j]>nums2[i2]:
                    r.append(nums2[j])
                    flag=1
                    break
            if flag==0:
                r.append(-1)
        return r
                        
