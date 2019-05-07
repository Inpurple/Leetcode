class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxlen=0
        chars = set()
        left,right=0,0
        while right<=len(s)-1:
            if s[right] not in chars:
                chars.add(s[right] )
                right=right+1
                maxlen=max(maxlen,len(chars))#只有一个字符的输入，没有此语句，会报错
            else:
                maxlen=max(maxlen,len(chars))
                if s[left] in chars:
                    chars.remove(s[left])
                    left+=1
        return maxlen
