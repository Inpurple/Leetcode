class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        字符串可以访问其中的值
        dict.values()以列表返回字典中的所有值
        """
        hashtable={}
        for i,letter in enumerate(s):
            valuelist=hashtable.values()
            if letter not in hashtable:
                hashtable[letter]=t[i]
                if t[i] in valuelist:#防止ad→aa
                    return False
            elif (hashtable[letter]!=t[i]):
                return False
        return True
