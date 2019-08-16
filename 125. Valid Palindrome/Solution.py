class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=""
        for  letter in s:
            if letter.isalpha() or letter.isnumeric() :
                res+=letter.lower()
        return res==res[-1::-1]
    
                
