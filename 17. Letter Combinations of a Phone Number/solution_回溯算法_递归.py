class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
                    }
        result=""
        res=[]
        if digits:
            self.dfs(digits,result,mapping,res)
            return res
        else:
            return res
        
    def dfs(self,digits,result,mapping,res):
        if not digits:
            res.append(result)
        else:
            for letter in mapping[digits[0]]:
                self.dfs(digits[1:],result+letter,mapping,res)     #此处需要传递参数
        
