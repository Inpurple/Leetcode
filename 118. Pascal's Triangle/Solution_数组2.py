class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lis=[]
        
        for i in range(1,numRows+1):
            sublist=[]
            for j in range(0,i):
                if j==0 or j==i-1:
                    sublist.append(1)
                else:
                    sublist.append(lis[i-1-1][j-1]+lis[i-1-1][j])
            lis.append(sublist)
            
        return lis
