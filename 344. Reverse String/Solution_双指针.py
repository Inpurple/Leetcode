class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        index1=0
        index2=len(s)-1
        
        while index1<index2:
            s[index1],s[index2]=s[index2],s[index1]
            index1+=1
            index2-=1
