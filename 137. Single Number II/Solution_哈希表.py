class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new={}
        for num in nums:
            if num not in new:
                new[num]=1
            elif new[num]==1:
                new[num]+=1
            else:
                del(new[num])
        #如果想获取键和值d.items方法会将键-值对作为二维元组返回，直接返回new.items()[0][0]也可以
        return new.items()[0][0]
            
