class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
                
        lis=sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return lis[0][0]
            
        
