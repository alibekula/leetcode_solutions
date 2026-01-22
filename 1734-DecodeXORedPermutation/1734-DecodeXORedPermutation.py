# Last updated: 22.01.2026, 07:30:12
1class Solution:
2    def decode(self, encoded: List[int]) -> List[int]:
3        
4        n = len(encoded) + 1
5
6        xor_1_to_nm1 = 0
7
8        for i in range(1, n+1):
9            xor_1_to_nm1 ^= i
10
11        first_xor = 0
12        for j in range(1, n-1, 2):
13            first_xor ^= encoded[j]
14        
15        first = xor_1_to_nm1 ^ first_xor
16
17        ans = [first]
18
19        for enc in encoded:
20            ans.append(ans[-1]^enc)
21        
22        return ans
23        
24
25        
26