# Last updated: 13.08.2025, 17:01:31
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows > len(s)-1:
            return s

        if len(s) == 1:
            return s

        rows = [''] * numRows
        curr_row = 0
        flag = False

        for char in s:
            rows[curr_row] += char

            if flag and curr_row == numRows -1:
                flag = not flag
            elif not flag and curr_row == 0:
                flag = not flag
            
            if flag:
                curr_row += 1
            else:
                curr_row -= 1

        return ''.join(rows)