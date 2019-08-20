class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #某些集合，每遍历一个数，增加这些集合
        
        print([]+[1])#应是[1]
        res=[[]]
        for num in nums:
            res=res+[[num]+array for array in res]#array已经是数组，故不需要在此子列表生成式中外加括号
            
        return res
