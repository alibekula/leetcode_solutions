# Last updated: 02.02.2026, 12:38:40
1class Solution:
2    class SmartWindow:
3        def __init__(self, k: int):
4            self.K = k
5            self.low = []   # sorted list
6            self.high = []  # sorted list
7            self.sumLow = 0
8
9        def windowSize(self) -> int:
10            return len(self.low) + len(self.high)
11
12        def _erase_one(self, arr: List[int], x: int) -> bool:
13            i = bisect_left(arr, x)
14            if i < len(arr) and arr[i] == x:
15                arr.pop(i)
16                return True
17            return False
18
19        def rebalance(self) -> None:
20            need = min(self.K, self.windowSize())
21
22            while len(self.low) > need:
23                x = self.low.pop()  # largest in low
24                self.sumLow -= x
25                insort(self.high, x)
26
27            while len(self.low) < need and self.high:
28                x = self.high.pop(0)  # smallest in high
29                insort(self.low, x)
30                self.sumLow += x
31
32        def add(self, x: int) -> None:
33            if not self.low or x <= self.low[-1]:
34                insort(self.low, x)
35                self.sumLow += x
36            else:
37                insort(self.high, x)
38            self.rebalance()
39
40        def remove(self, x: int) -> None:
41            if self._erase_one(self.low, x):
42                self.sumLow -= x
43            else:
44                self._erase_one(self.high, x)
45            self.rebalance()
46
47        def query(self) -> int:
48            return self.sumLow
49
50    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
51        n = len(nums)
52        k -= 1
53        window = self.SmartWindow(k)
54
55        for i in range(1, 1 + dist + 1):
56            window.add(nums[i])
57
58        ans = window.query()
59
60        for i in range(2, n - dist):
61            window.remove(nums[i - 1])
62            window.add(nums[i + dist])
63            ans = min(ans, window.query())
64
65        return ans + nums[0]