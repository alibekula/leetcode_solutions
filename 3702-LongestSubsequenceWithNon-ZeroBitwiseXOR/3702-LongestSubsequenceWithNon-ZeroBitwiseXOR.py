# Last updated: 24.01.2026, 01:15:45
1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        n = len(nums)
4        
5        # Calculate the XOR of all elements
6        total_xor = 0
7        for x in nums:
8            total_xor ^= x
9            
10        # Case 1: If the total XOR is already non-zero, 
11        # the longest subsequence is the whole array.
12        if total_xor != 0:
13            return n
14            
15        # Case 2: If total XOR is 0, we check if we can remove just one element.
16        # If there is ANY non-zero element in nums, removing it will make 
17        # the remaining XOR non-zero (because 0 ^ x = x).
18        for x in nums:
19            if x != 0:
20                return n - 1
21                
22        # Case 3: If all elements are 0, it's impossible to get a non-zero XOR.
23        return 0