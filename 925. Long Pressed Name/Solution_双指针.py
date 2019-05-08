class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        types=[]
        j=0
        for i in range(0,len(typed)):#主迭代

            if j<=len(name)-1 and typed[i]==name[j]:
                j=j+1

            elif j<=len(name)-1 and typed[i]!=name[j]:
                if typed[i-1]==typed[i]:
                    continue
                else:
                    return False
            #i 依然在遍历，但是j已经输入完,这种情况题目未考虑，也能通过
            
            
        if j==len(name):#排除还有j，但是typed已经遍历完得情况

            return True
 
