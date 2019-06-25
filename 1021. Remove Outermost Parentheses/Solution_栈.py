class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res=""
        sta=[]
        for i in S:
            sta.append(i)
            if sta.count('(')==sta.count(')'):
                res=res+"".join(sta[1:-1])
                sta=[]
        return res
                    
