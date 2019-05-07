class Solution(object):
    import copy
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for  i in range(len(board)):
            for j in range(len(board[0])):
                if self.dnf(i,j,board,word):
                    return True#这种结构可以避免多余的搜索
        return False
                
        

        
    def dnf(self,i,j,board,word):
        if not word:
            return True
        elif i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or word[0]!=board[i][j]:#注意位置，应该先检查索引的范围再取值
            return False
        tmp=board[i][j]
        board[i][j]=""#tmp是字符串的数据结构，tmp改变，board[i][j]未跟着改变
     
        if self.dnf(i+1,j,board,word[1:]) or self.dnf(i,j+1,board,word[1:]) or self.dnf(i-1,j,board,word[1:]) or self.dnf(i,j-1,board,word[1:]):
            return True
        board[i][j]=tmp
        return False
