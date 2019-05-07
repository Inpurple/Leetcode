import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.match(p+'$', s)!=None
        #p如果去掉'$'会导致输入"aa""a"不通过
        #'$'匹配字符串末尾
