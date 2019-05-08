class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index1=0
        index2=len(s)-1
        
        s= list(s)
        vowels="aeoiuAEOIU"
        while index1<index2:
            if s[index1] not in vowels:
                index1+=1
                continue
            if s[index2] not in vowels:
                index2-=1
                continue
            elif s[index1] in vowels and s[index2] in vowels:
                s[index1],s[index2]=s[index2],s[index1]
                index1+=1
                index2-=1
        s=''.join(s)
        return s
