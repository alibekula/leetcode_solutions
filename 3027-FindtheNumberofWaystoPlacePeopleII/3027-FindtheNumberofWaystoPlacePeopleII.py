# Last updated: 28.09.2025, 07:03:50
class Solution:
    def numberOfPairs(self, P: List[List[int]]) -> int:
        
        P.sort(key = lambda x: (-x[0], x[1]))

        ans, n = 0, len(P)

        for i in range(n-1):
            y_max, y_min = float('inf'), P[i][1]

            for j in range(i+1, n):
                
                y = P[j][1]

                if y_max > y >= y_min:
                    ans += 1
                    y_max = y
                    if y == y_min:
                        break
        
        return ans