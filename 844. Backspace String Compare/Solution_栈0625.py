class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        staS=self.trans(S)
        staT=self.trans(T)
        while staS and staT:
            if staS.pop()!= staT.pop():
                return False
        if staS or staT:
            return False
        else:
            return True
        #是否可以直接比较栈？？
        
    def trans(self,A):
        sta=[]
        for letter in A:
            if letter=="#" and sta:
                sta.pop()
            elif letter!="#":
                sta.append(letter)
        return sta
 
