# Last updated: 13.08.2025, 16:56:41
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = {0:1}
        curr = 0
        count = 0

        for num in nums:
            curr += num

            if curr%k in pref:
                count += pref[curr%k]
                pref[curr%k] += 1
            else:
                pref[curr%k] = 1
    
        return count
