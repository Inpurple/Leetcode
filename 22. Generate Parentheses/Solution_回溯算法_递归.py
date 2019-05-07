class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n or n==0:
            return []
        else:
            result=[]
            self.dnf(n,n,"",result)
            return result
            
    def dnf(self,left,right,tmp,result):
        if left<0 or right<0 or left-right>0:
            return None
        elif left==0 and right==0:
            result.append(tmp)
        else:
            self.dnf(left-1,right,tmp+"(",result)
            self.dnf(left,right-1,tmp+")",result)
