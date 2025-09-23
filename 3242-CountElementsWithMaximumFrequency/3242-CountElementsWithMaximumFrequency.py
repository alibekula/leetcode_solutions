# Last updated: 23.09.2025, 16:40:19
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        max_count_key = max(counter, key=lambda x: counter[x])
        max_count = counter[max_count_key]

        n = 0

        for val in counter.values():
            if val == max_count:
                n += 1
        
        return n * max_count