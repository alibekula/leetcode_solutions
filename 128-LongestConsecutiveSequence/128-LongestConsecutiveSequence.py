# Last updated: 13.08.2025, 16:59:31
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 1 if nums else 0

        for i in sett:
            l = 1
            if i - 1 not in sett:
                while i + l in sett:
                    l += 1
                longest = max(longest, l)
       
        return longest
