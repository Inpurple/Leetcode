class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p and not s:
            return True
        elif not p and s:#p能自删除，但是s不能，说明此情况s未全包含
            return False
        
            
        firstmatch=bool(s)and(s[0]==p[0] or p[0]=='.')#如果s没有了只能考虑自删除
        if len(p)>=2 and p[1]=='*':
            return self.isMatch(s,p[2:]) or (firstmatch and self.isMatch(s[1:],p) )
            
        else:#位置很重要，
            return firstmatch and self.isMatch(s[1:],p[1:])
        
        
        """
        如果写成
        if len(p)>=2 and p[1]！='*':#需要考虑p只有一个的情景，会出现错误的答案
            return firstmatch and self.isMatch(s[1:],p[1:])
            
        else:#两种写法位置很重要，
            return self.isMatch(s,p[2:]) or (firstmatch and self.isMatch(s[1:],p) )
            
        

        """
