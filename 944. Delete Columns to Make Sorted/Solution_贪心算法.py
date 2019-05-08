class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        D=[]
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i+1<len(A) and A[i+1][j]<A[i][j] and j not in D:#只要有降序就删除，避免同一列再次碰到降序重复删除的情况
                        D.append(j)
        return len(D)
