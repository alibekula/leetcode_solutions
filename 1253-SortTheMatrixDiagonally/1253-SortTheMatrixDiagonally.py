# Last updated: 13.08.2025, 16:56:36
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        row, col = len(mat)-1, len(mat[0])-1
        new_mat = [[0]*len(mat[0]) for _ in range(row+1)]

        def sort_diag( i, j, diag=None):

            diag.append(mat[i][j])
            
            if i == row or j == col:
                diag.sort()
                return diag
            
            diag = [] if diag is None else diag
            return sort_diag(i+1, j+1, diag)
        
        for m in range(col+1):
            diagonal = sort_diag(0, m, [])
            i = 0
            j = m
            
            for item in diagonal:
                new_mat[i][j] = item
                i += 1
                j += 1
        
        for n in range(1, row + 1):
            diagonal = sort_diag(n, 0, [])
            i = n
            j = 0
            
            for item in diagonal:
                new_mat[i][j] = item
                i += 1
                j += 1


        return new_mat







        