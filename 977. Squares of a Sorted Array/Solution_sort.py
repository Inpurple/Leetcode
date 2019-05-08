class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        双指针尝试变复杂了 从两边到中间，谁的绝对值大谁就往前进一位
        Sort方法时间复杂度为O（N）
        """
        for i in range(len(A)):
            A[i]=A[i]*A[i]
            
        A.sort()
        
        return A
