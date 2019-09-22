class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid==[[0]]:
            return 2
        root=((0,0),grid[0][0],1)#
        que=[root]
        if root[1]==1:
            return -1
        dic={}
        while que:
            curnode=que.pop(0)
            dic[curnode[0]]=1
            i=curnode[0][0]
            j=curnode[0][1]
            lis=[(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]
            for nex in lis:
                if nex[0]>len(grid)-1 or nex[0]<0 or nex[1]>len(grid)-1  or nex[1]<0:
                    continue
                if grid[nex[0]][nex[1]]==1:
                    continue
                if nex in dic:
                    continue
                if nex[0]==len(grid)-1 and nex[1]==len(grid)-1:
                    return curnode[2]+1
                else:
                    que.append((nex,0,curnode[2]+1)) 
                print(nex)
        return -1


        
