# Last updated: 17.12.2025, 22:15:11
1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        
4        counter1 = {}
5        counter2 = {}
6        n, m = len(s), len(p)
7        ans = []
8
9        if n < m:
10            return []
11
12        for char in s[:m]:
13            counter1[char] = counter1.get(char, 0) + 1
14        
15        for char in p:
16            counter2[char] = counter2.get(char, 0) + 1
17        
18        difference = 0
19
20        for key in counter2:
21            if key in counter1:
22                if counter1[key] != counter2[key]:
23                    difference += 1
24            else:
25                difference += 1
26        
27        if difference == 0:
28            ans.append(0)
29
30        for i in range(1, n-m+1):
31            left_char = s[i-1]
32            right_char = s[i + m-1]
33
34            if left_char in counter2 and counter2[left_char] == counter1[left_char]:
35                difference += 1
36            
37            if right_char in counter2 and counter2[right_char] == counter1.get(right_char, 0):
38                difference += 1
39
40            counter1[left_char] -= 1
41            counter1[right_char] = counter1.get(right_char, 0) + 1
42
43            if counter1[left_char] == 0:
44                del counter1[left_char]
45
46            else:
47                if left_char in counter2 and counter1[left_char] == counter2[left_char]:
48                    difference -= 1
49            
50            if right_char in counter2:
51                if counter2[right_char] == counter1[right_char]:
52                    difference -= 1
53            
54            if difference == 0:
55                ans.append(i)
56        
57        return ans
58
59