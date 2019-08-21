class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for word in strs:
            key=str(sorted(word))#注意尽管word是str类型，但sorted()之后返回的是list类型
            
            if key not in dic:
                dic[key]=[word]
            else:
                dic[key].append(word)
                
        return dic.values()
        
