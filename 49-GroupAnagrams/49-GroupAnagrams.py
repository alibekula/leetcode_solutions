# Last updated: 16.12.2025, 17:56:05
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4        hashmap = {}
5
6        for s in strs:
7            key = [0] * 30
8            for char in s:
9                key[ord(char) - ord('a')] += 1
10            
11            key = tuple(key)
12            hashmap[key] = hashmap.get(key, [])
13            hashmap[key].append(s)
14        
15        return list(hashmap.values())