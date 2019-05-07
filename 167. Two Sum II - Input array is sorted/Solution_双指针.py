class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1=0
        index2=len(numbers)-1
        while numbers[index1]+numbers[index2]!=target:
            if numbers[index1]+numbers[index2]>target:
                index2=index2-1
            else:
                index1=index1+1
        return[index1+1,index2+1]
