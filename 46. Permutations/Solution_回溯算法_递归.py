class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        else:
            result=[]
            self.dnf(nums,[],result)
            return result
        
    def dnf(self,nums,tmp,result):
        if not nums:
            result.append(tmp)
            return
        else:
            for i,num in enumerate(nums):
                _nums=nums[:]#选择列表的克隆，不要修改正在遍历列表，会在同一行中产生矛盾
                _nums.remove(num)#此函数的返回值为None
                print(nums)
                print(_nums)
                self.dnf(_nums,tmp+[num],result)#列表的相加，返回列表：tmp+[num]；列表的删除，返回列表：nums[:i]+nums[i+1:]
