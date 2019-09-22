class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        elif len(grid) <= 2:#题目测试问题的解决方法
            return len(grid)
        root=((0,0),1)#
        que=[root]
        while que:
            curnode=que.pop(0)
            i=curnode[0][0]
            j=curnode[0][1]
            lis=[(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]
            for x,y in lis:#用x,y 不要用某一个值再去查找索引的值会变慢
                if x>len(grid)-1 or x<0 or y>len(grid)-1  or y<0:
                    continue
                if grid[x][y]==1:
                    continue
                if x==len(grid)-1 and y==len(grid)-1:
                    return curnode[1]+1
                else:
                    que.append(((x,y),curnode[1]+1)) 
                    grid[x][y]=1
        return -1
