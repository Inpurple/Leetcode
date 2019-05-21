class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        small=0
        large=len(nums)-1
        count=0
        while small<large :#分为单个数字之前进行循环
            print(nums[(large+small)//2])
            print(nums[small],nums[large])
            if nums[(large+small)//2]<target:
                small=(large+small)//2+1#如果只有两个元素去划分，如果small=(large+small)//2，无法将两种情况划分为单个元素

            elif nums[(large+small)//2]>target:
                large=(large+small)//2
            else:
                return (large+small)//2
        if nums[(large+small)//2]==target:
            return (large+small)//2
        else:
            return -1
