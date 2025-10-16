# Last updated: 16.10.2025, 23:24:24
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = Counter(num % value for num in nums)

        m = 0
        while True:
            r = m % value
            if counts[r] == 0:
                return m
            counts[r] -= 1
            m += 1
