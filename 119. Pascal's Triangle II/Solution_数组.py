class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        for i in range(1,rowIndex+2):
            if i==1:
                lis=[1]
            elif i==2:
                lis=[1,1]
            else:
                for k in range(1,i-1):
                    w=prelis[k]+prelis[k-1]
                    lis[k]=w
                lis.append(1)
            prelis=lis[:]#要注意此处是列表的克隆，若直接赋值则pre，lis指的是一个列表
        return lis
            
