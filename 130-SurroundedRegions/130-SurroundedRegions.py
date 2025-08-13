# Last updated: 13.08.2025, 16:59:28
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def expand(r, c):
            if (r < 0 or r >= n) or (c < 0 or c >= m) or board[r][c] != 'O':
                return 
            
            board[r][c] = 'S'

            expand(r+1, c)
            expand(r-1, c)
            expand(r, c+1)
            expand(r, c-1)
        
        for i in range(n):
            if board[i][0] == 'O':
                expand(i, 0)
            if board[i][m-1] == 'O':
                expand(i, m-1)
        
        for j in range(m):
            if board[0][j] == 'O':
                expand(0, j)
            if board[n-1][j] =='O':
                expand(n-1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X' 