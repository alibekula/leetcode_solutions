# Last updated: 23.01.2026, 06:19:35
1class Solution:
2    def build_tree(self, dictionary):
3        root = {}
4        for word in dictionary:
5            node = root
6            for char in word:
7                if char not in node:
8                    node[char] = {}
9                node = node[char]
10            node['#'] = True
11        return root
12            
13    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
14        tree = self.build_tree(dictionary)
15
16        def search(word, idx, node, errors):
17            if errors > 2:
18                return False
19            if idx == len(word):
20                return '#' in node
21            
22            char = word[idx]
23
24            if char in node:
25                if search(word, idx + 1, node[char], errors):
26                    return True
27            
28            if errors < 2:
29                for nei in node:
30                    if nei == '#' or nei == char:
31                        continue
32                    
33                    if search(word, idx + 1, node[nei], errors + 1):
34                        return True
35            
36            return False
37        
38        ans = []
39        for q in queries:
40            if search(q, 0, tree, 0):
41                ans.append(q)
42        
43        return ans