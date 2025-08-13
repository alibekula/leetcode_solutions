# Last updated: 13.08.2025, 16:58:00
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_sum = 0
                
                for dx, dy in directions:
                    if (dx + i >= 0 and dx + i < len(board)) and (dy + j >= 0 and dy + j < len(board[0])): 
                        if board[dx +i][dy + j] in (-1, 1):
                            curr_sum += 1
                
                if board[i][j] == 0:
                    if curr_sum == 3:
                        board[i][j] = 2
                else:
                    if curr_sum < 2:
                        board[i][j] = -1
                    elif curr_sum in (2, 3):
                        board[i][j] = 1
                    elif curr_sum > 3:
                        board[i][j] = -1


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

        