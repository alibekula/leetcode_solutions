# Last updated: 25.01.2026, 22:56:34
1class Solution:
2    def checkIfPangram(self, sentence: str) -> bool:
3        
4        dct = {}
5
6        for i in range(ord('a'), ord('z')+1):
7            dct[i] = 0
8        
9        for char in sentence:
10            dct[ord(char)] += 1
11        
12        for num in dct:
13            if dct[num] == 0:
14                return False
15        
16        return True
17