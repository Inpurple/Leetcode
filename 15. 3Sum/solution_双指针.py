class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #用双指针做比用哈希表做两数之和的好处是，更好的剔除相同的情况。
        哈希表不合适，长时间做不出来
        """
        nums.sort()
        solution=[]
        for index1 in range(0,len(nums)-2):
            index2=index1+1
            index3=len(nums)-1
            if index1>=1 and nums[index1]==nums[index1-1]:
                continue
            while index2<index3:
                if index2>=index1+2 and nums[index2]==nums[index2-1]:
                    index2=index2+1
                    continue
                if index3+1<=len(nums)-1 and nums[index3+1]==nums[index3]:
                    index3=index3-1
                    continue
                if nums[index1]+nums[index2]+nums[index3]==0:
                    solution.append([nums[index1],nums[index2],nums[index3]])
                    index3=index3-1
                    index2=index2+1
                elif nums[index1]+nums[index2]+nums[index3]>0:
                    index3=index3-1
                elif nums[index1]+nums[index2]+nums[index3]<0:
                    index2=index2+1
                
        return solution
