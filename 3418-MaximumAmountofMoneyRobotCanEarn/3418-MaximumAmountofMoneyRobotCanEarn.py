# Last updated: 25.01.2026, 02:22:39
1import sys
2
3# Важно: поднимаем лимит рекурсии
4sys.setrecursionlimit(20000)
5
6class Solution:
7    def maximumAmount(self, coins: List[List[int]]) -> int:
8        n, m = len(coins), len(coins[0])
9        
10        # Вместо словаря используем массив.
11        # Инициализируем None. Если там None — значит, еще не считали.
12        memo = [[[None] * 3 for _ in range(m)] for _ in range(n)]
13
14        def dfs(i, j, k):
15            if i >= n or j >= m:
16                return float('-inf')
17
18            # Проверка в массиве быстрее, чем хеширование в словаре
19            if memo[i][j][k] is not None:
20                return memo[i][j][k]
21
22            val = coins[i][j]
23
24            # База: финиш
25            if i == n - 1 and j == m - 1:
26                if val < 0 and k > 0:
27                    return 0
28                return val
29
30            val_pos = val + max(dfs(i + 1, j, k), dfs(i, j + 1, k))
31
32            val_neg = float('-inf')
33            if val < 0 and k > 0:
34                val_neg = 0 + max(dfs(i + 1, j, k - 1), dfs(i, j + 1, k - 1))
35
36            res = max(val_pos, val_neg)
37            
38            memo[i][j][k] = res
39            return res
40
41        return dfs(0, 0, 2)