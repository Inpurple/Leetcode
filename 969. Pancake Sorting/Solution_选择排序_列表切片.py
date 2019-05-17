class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        参数复杂：
        反转方法一：反转i+1：A[0:i+1]=A[i::-1]
        反转方法二：反转3：a[0:3] = list(reversed(a[0:3]))
        算法利用选择排序的思想
        """
        
        r=[]
        for i in range(len(A)-1,0,-1):
            m=float("-inf")
            for j in range(0,i+1):
                if A[j]>m:
                    m=A[j]
                    m_i=j
            if m_i==0:
                r.append(i+1)
                A[0:i+1]=A[i::-1]
            elif m_i==i:
                pass
            else:
                r.append(m_i+1)
                A[0:m_i+1]=A[m_i::-1]
                r.append(i+1)
                A[0:i+1]=A[i::-1]
        
        return r
