class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        p
        """
        
        D=[]
        #先比较第一行和第二行，真正运用到了可以步骤可以重复的贪心算法
        #试一下for rangelen(A) 迭代，是否可以删除A中的元素，如果不能，改为while---删除列表中字符串的某一字母很复杂
        #如果在debug的使用需要print，提交记得删除，因为print会耗时
        n=0

        while n<=len(A)-2:            #for n in range(0,len(A)-1):
            
            for m in range(0,len(A[0])):

                if m in D:#很巧妙的方法避开删除元素这么艰难的操作，并且可以去重
                    continue
                elif A[n][m]>A[n+1][m]:
                    D.append(m)
                    n=-1#一列中，先是对的，下面的排序非字典序需要删除，然后要从头开始，其实可以不从头开始
                    break
                elif A[n][m]==A[n+1][m]:#
                    pass#相等或者是删除行，这里用continue 也可以
                else:
                    break
            n=n+1

        return len(D)
         
