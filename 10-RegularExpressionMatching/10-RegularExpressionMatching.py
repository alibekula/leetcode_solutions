# Last updated: 10.09.2025, 06:53:00
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}

        def sp_match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == m:
                return i == n

            first = i < n and (s[i] == p[j] or p[j] == '.')

            if j+1 < m and p[j+1] == '*':
                res = sp_match(i, j+2) or (first and sp_match(i+1, j))
            else:
                res = first and sp_match(i+1, j+1)

            memo[(i, j)] = res
            return res

        return sp_match(0, 0)
