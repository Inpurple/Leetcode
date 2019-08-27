class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res=[]
        self.dfs([s])
        return self.res
        
    def dfs(self,temp):
        flag=1
        for string in temp:
            if string!=string[::-1]:
                flag=0
                break
        if flag==1:
            self.res.append(temp)
        st=temp[-1]
        
        for i in range(0,len(st)-1):
            
            k=st[0:i+1]
            if k!=k[::-1]:
                continue
            copytemp=temp[:]
            copytemp[-1]=st[0:i+1]
            copytemp.append(st[i+1:len(st)])
            
            self.dfs(copytemp)
