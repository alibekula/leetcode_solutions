# Last updated: 13.08.2025, 16:57:44
class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        counter = Counter(nums)
        unique_nums = len(counter)
        min_count = 1
        max_count = n - (unique_nums - 1)
        dct = {key:[] for key in range(min_count, max_count+1)}

        for key, value in counter.items():

            dct[value].append(key)

        ans = []

        for key in range(max_count, min_count-1, -1):
            for item in dct[key]:
                ans.append(item)
                if len(ans) == k:
                    return ans
