class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k=self.recur(n,[])
        return k
        
    def recur(self,n,lis):
        s=0
        lis.append(n)
        for i in str(n):
            s=s+int(i)**2
        print(s)
        if int(s)==int(1):
            return True
        elif s in lis:#无限循环的条件是出现了曾经的值，然后一直循环
            return False
        else:
            return self.recur(s,lis)###return 忘记写，直接导致最后返回None
