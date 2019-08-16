class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        首索引 x+k-1=len(nums)-1 -> x=len(nums)-k
        末索引 y+k=len(nums)-1  ->  y=len(nums)-k-1
        
        """
        
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        #如果写成nums=nums[len(nums)-k:]+nums[:len(nums)-k] nums没有改变
