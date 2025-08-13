# Last updated: 13.08.2025, 16:56:07
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even, odd, even_odd, odd_even = (0, 0, 0, 0)

        for x in nums:
            if x%2:
                odd += 1
                odd_even = max(odd_even, even_odd+1)
            else:
                even += 1
                even_odd = max(odd_even + 1, even_odd)

        return max(even, odd, even_odd, odd_even)