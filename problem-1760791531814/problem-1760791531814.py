# Last updated: 18.10.2025, 18:45:31
class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        used = set()
        last = -10**18  # минимальное возможное значение
        
        for num in nums:
            # возможная минимальная позиция, не занятая раньше
            start = max(num - k, last + 1)
            if start <= num + k:
                used.add(start)
                last = start
        
        return len(used)
