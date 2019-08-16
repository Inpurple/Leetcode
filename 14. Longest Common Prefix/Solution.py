class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        i=0
        if not strs:
            return res
        
        
        while i<=len(strs[0])-1:#
            k=strs[0][i]
            for st in strs:
                if i>=len(st) or st[i]!=k:
                    return res
            res+=k
            i+=1
            
        return res
            
    
