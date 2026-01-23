# Last updated: 24.01.2026, 02:26:46
1class Solution:
2    def tictactoe(self, moves: List[List[int]]) -> str:
3        mat = [[''] * 3 for _ in range(3)]
4        mark = 'X'
5        for row, col in moves:
6            mat[row][col] = mark
7            mark = 'O' if mark == 'X' else 'X'
8
9        def find_winner(string):
10            if string in ['XXX', 'OOO']:
11                if string[0] == 'X':
12                    return 'A'
13                else:
14                    return 'B'
15            else:
16                return False
17
18        rows, cols = [], []
19        main_diag, side_diag = '', ''
20
21
22        for i in range(3):
23            row = ''.join(mat[i])
24            col = ''.join([mat[j][i] for j in range(3)])
25
26            rows.append(row)
27            cols.append(col)
28            main_diag += mat[i][i]
29            side_diag += mat[i][2-i]
30        
31        sides = rows + cols + [main_diag, side_diag]
32
33        for side in sides:
34            res = find_winner(side)
35
36            if res:
37                return res
38        
39        if len(moves) == 9:
40            return 'Draw'
41        
42        return 'Pending'