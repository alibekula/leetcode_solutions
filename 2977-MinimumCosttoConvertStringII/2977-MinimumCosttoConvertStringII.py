# Last updated: 30.01.2026, 07:12:04
1class Solution:
2    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
3        import sys
4
5class TrieNode:
6    def __init__(self):
7        # В C++ использовался массив children[26], в Python удобнее словарь,
8        # но для точности перевода можно использовать список
9        self.children = [None] * 26
10        self.id = -1
11
12class Trie:
13    def __init__(self):
14        self.root = TrieNode()
15        self.id_counter = 0
16
17    def insert(self, s: str) -> int:
18        node = self.root
19        for char in s:
20            idx = ord(char) - ord('a')
21            if not node.children[idx]:
22                node.children[idx] = TrieNode()
23            node = node.children[idx]
24        
25        # Если у подстроки еще нет ID, присваиваем новый
26        if node.id == -1:
27            node.id = self.id_counter
28            self.id_counter += 1
29        return node.id
30    
31    def get_root(self):
32        return self.root
33    
34    def count(self):
35        return self.id_counter
36
37class Solution:
38    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
39        trie = Trie()
40
41        # 1. Маппинг всех подстрок в уникальные ID через Trie
42        # Это нужно, чтобы превратить задачу работы со строками в задачу работы с графом (числами)
43        for s in original:
44            trie.insert(s)
45        for s in changed:
46            trie.insert(s)
47
48        n = trie.count()
49        
50        # Инициализация матрицы смежности для Флойда-Уоршелла
51        # dist[u][v] хранит минимальную стоимость превращения подстроки с ID u в ID v
52        inf = float('inf')
53        dist = [[inf] * n for _ in range(n)]
54
55        for i in range(n):
56            dist[i][i] = 0
57
58        # Заполняем начальные веса из условий задачи
59        for i in range(len(original)):
60            u = trie.insert(original[i])
61            v = trie.insert(changed[i])
62            dist[u][v] = min(dist[u][v], cost[i])
63
64        # 2. Алгоритм Флойда-Уоршелла
65        # Находим кратчайшие пути между всеми парами подстрок
66        # Это нужно для транзитивности: "a" -> "b" -> "c"
67        for via in range(n):
68            for start in range(n):
69                if dist[start][via] == inf:
70                    continue
71                for end in range(n):
72                    if dist[via][end] == inf:
73                        continue
74                    if dist[start][end] > dist[start][via] + dist[via][end]:
75                        dist[start][end] = dist[start][via] + dist[via][end]
76
77        # 3. Динамическое программирование (DP)
78        m = len(source)
79        # dp[i] = минимальная стоимость превращения префикса source[:i] в target[:i]
80        dp = [inf] * (m + 1)
81        dp[0] = 0
82
83        for i in range(m):
84            if dp[i] == inf:
85                continue
86            
87            # Вариант А: Символы совпадают, можно ничего не менять (бесплатно)
88            if source[i] == target[i]:
89                dp[i + 1] = min(dp[i + 1], dp[i])
90            
91            # Вариант Б: Пытаемся применить замену подстроки, начинающейся в i
92            # Одновременно спускаемся по Trie для source и target
93            p_s = trie.get_root()
94            p_t = trie.get_root()
95
96            for j in range(i, m):
97                char_s_idx = ord(source[j]) - ord('a')
98                char_t_idx = ord(target[j]) - ord('a')
99
100                p_s = p_s.children[char_s_idx]
101                p_t = p_t.children[char_t_idx]
102
103                # Если хотя бы одной из подстрок нет в Trie, дальше идти нет смысла
104                if not p_s or not p_t:
105                    break
106                
107                # Если обе подстроки (source[i...j] и target[i...j]) существуют в наших правилах (имеют ID),
108                # проверяем, можно ли превратить одну в другую
109                if p_s.id != -1 and p_t.id != -1:
110                    u = p_s.id
111                    v = p_t.id
112                    if dist[u][v] != inf:
113                        # dp[начало] + стоимость превращения куска
114                        dp[j + 1] = min(dp[j + 1], dp[i] + dist[u][v])
115
116        return dp[m] if dp[m] != inf else -1