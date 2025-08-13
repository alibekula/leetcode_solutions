# Last updated: 13.08.2025, 16:58:39
class Solution:

    def build_tree(self,arr):
        dct = {}

        for word in arr:
            curr = dct
            for char in word:
                if char not in curr:
                    curr[char] = dict()
                
                curr = curr[char]
            curr['#'] = word
        
        return dct


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = self.build_tree(words)
        n, m = len(board), len(board[0])
        res = []

        def search(i, j, leaf):
            
            char = board[i][j]

            if char not in leaf:
                return
            
            next_node = leaf[char]
            word = next_node.pop('#', None)

            if word:
                res.append(word)

            board[i][j] = '.'

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                di, dj = i+dx, j+dy

                if 0 <= di < n and 0 <= dj < m and board[di][dj] != '.':
                    search(i+dx, j+dy, next_node)
            
            board[i][j] = char

            if not leaf[char]:
                del leaf[char]


        for i in range(n):
            for j in range(m):
                search(i, j, tree)
        
        return res