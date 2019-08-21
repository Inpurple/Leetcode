class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=1
            elif num in dic:
                return num
