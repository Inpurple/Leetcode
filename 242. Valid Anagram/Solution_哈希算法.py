class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        approach2：hashmap
        Complexity analysis

Time complexity : O(n)O(n). Time complexity is O(n)O(n) because accessing the counter table is a constant time operation.

Space complexity : O(1)O(1). Although we do use extra space, the space complexity is O(1)O(1) because the table's size stays constant no matter how large nn is.

        
        """
        dics={}
        dictt={}
        for letter in s:
            if letter not in dics:
                dics[letter]=1
            else:
                dics[letter]+=1
                
        for letter in t:
            if letter not in dictt:
                dictt[letter]=1
            else:
                dictt[letter]+=1
                
        return (dictt==dics)
