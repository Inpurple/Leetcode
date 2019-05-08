    class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        t=list(t)
        for j in range(1,len(s)):
            for k in range(j,-1,-1):
                if s[k]<s[k-1]:
                    s[k],s[k-1]=s[k-1],s[k]

        for j in range(1,len(t)):
            for k in range(j,-1,-1):
                if t[k]<t[k-1]:
                    t[k],t[k-1]=t[k-1],t[k]
    
       #插入排序的时间复杂度为O(n**n)
        if t==s:
            return True
        else:
            return False
