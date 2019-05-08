class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        用堆栈或者切片做
        """
        return self.transform(S)==self.transform(T)
        
        
        
        
    def transform(self,a):
        inputa=""
        for i in a:
            if i!='#':
                inputa=inputa+i
            else:
                if inputa:
                    inputa=inputa[:-1]
        return inputa
