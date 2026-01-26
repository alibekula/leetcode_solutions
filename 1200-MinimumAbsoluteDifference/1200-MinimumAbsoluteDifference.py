# Last updated: 26.01.2026, 07:16:10
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        
4        # a b c d ab ac ad bc bd cd
5        # n! / ((n-k)! * k!)
6
7        sett = set(arr)
8        min_diff = float('inf')
9
10        arr.sort()
11        n = len(arr)
12
13        for i in range(n-1):
14            j = i +1
15
16            min_diff = min(min_diff, abs(arr[j] - arr[i]))
17        
18        ans = []
19        deleted = set()
20
21        for num in sett:
22            
23            left = num + min_diff
24            right = num - min_diff
25
26            if num in deleted:
27                continue
28            deleted.add(num)
29
30            if left in sett and left not in deleted:
31                ans.append([num, num+min_diff])
32            
33            if right in sett and right not in deleted:
34                ans.append([num-min_diff, num])
35        
36        return sorted(ans)
37
38
39
40         
41            