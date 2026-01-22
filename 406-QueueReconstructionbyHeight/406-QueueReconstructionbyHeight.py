# Last updated: 23.01.2026, 04:20:15
1class Solution:
2    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
3
4        people.sort(key=lambda x: (-x[0], x[1]))
5        ans = []
6
7        for h, k in people:
8            ans.insert(k, [h,k])
9        
10        return ans
11
12
13
14