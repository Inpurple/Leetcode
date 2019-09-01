class Solution:
    def numSquares(self, n: int) -> int:
        que=[(n,1)]
        visited=[False for __ in range(n+1)]#注意n+1
        visited[n]=True#优化出现过的值
        while que:
            pre=que.pop(0)
            i=1
            while i**2<=pre[0]:
                cur=pre[0]-i**2
                if cur==0:
                    return pre[1]
                if visited[cur]==False:
                    que.append((cur,pre[1]+1))
                    visited[cur]=True
                i=i+1
                
