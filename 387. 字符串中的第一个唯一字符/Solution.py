class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            if s[i] not in s.replace(s[i],'_',1) :#replace方法中，第三个参数不填表示全局替换。并且replace方法返回替换后的s，而不改变s
                return i
            
        return -1
