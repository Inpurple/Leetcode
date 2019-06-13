class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dic={
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        
        for i in s:
            if i in dic:
                stack.append(i)
            elif not stack:#排除"]"的情况
                return False
            elif  dic[stack.pop()]!=i:
                return False
        if stack:
            return False#排除"["的情况
        else:
            return True
