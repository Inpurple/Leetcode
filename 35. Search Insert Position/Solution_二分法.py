class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        small=0
        large=len(nums)-1
        count=0
        while target!=nums[int((small+large)/2)] and abs((small+large)/2.000-int((small+large)/2))>=0.25:
            count+=1
            if target<nums[int((small+large)/2)]:
                large=(small+large)/2 #（1+2）/2=1.5 1+1.5 /2=1.25 ;1,3,4 找2 0+1.25 /2 =5.125
            else:
                small=(small+large)/2
        print(count)
        if target==nums[int((small+large)/2)]:
            return int(small+large)/2
        else:
            nums.insert(int(small),'target')
            return 0
