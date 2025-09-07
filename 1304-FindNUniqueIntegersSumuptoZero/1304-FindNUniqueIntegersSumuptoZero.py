# Last updated: 07.09.2025, 20:20:49
memo = {1:[0]}
for i in range(1, 1000):
    curr = []
    for j in range(1, i+2):
        curr.append(j)

    total = sum(curr) - curr[-1]
    curr[-1] = -total
    memo[i+1] = curr[:]


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return memo[n]
        