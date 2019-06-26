class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic={}
        for i in tasks:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        maxcount=max(dic.values())
        maxsame=0
        
        for j in dic.keys():
            if dic[j]==maxcount:
                maxsame+=1
        
        
        res=(maxcount-1)*(n+1)+maxsame
        
        if res<len(tasks):
            return len(tasks)
        else:
            return res
