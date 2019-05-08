class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        while K>0:
            minnum=min(A)
            minindex=A.index(minnum)
            A[minindex]=0-A[minindex]
            K=K-1
        s=sum(A)
        return s
