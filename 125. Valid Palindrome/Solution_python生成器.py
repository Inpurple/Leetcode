class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=[x.lower() for x in s if x.isalnum()]#python生成器
        return res==res[::-1]#列表反转，res[-1::-1]==res[::-1]
    
                
                
        
