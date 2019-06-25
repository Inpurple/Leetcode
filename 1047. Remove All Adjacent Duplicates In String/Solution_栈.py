class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        sta=[]
        for i in S:
            if sta and sta[-1]==i:
                sta.pop()
            else:
                sta.append(i)
        return ''.join(sta)
    
                
