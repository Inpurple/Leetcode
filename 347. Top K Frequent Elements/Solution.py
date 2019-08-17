class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset=set(nums)
        dic={}
        for num in numset:
            dic[num]=nums.count(num)
            
        res=sorted(dic.(),key=lambda dic:dic[1],reverse=True)
        
        return [i[0] for i in res[0:k]]
        
        
        
        """
        可关注heap
        """
