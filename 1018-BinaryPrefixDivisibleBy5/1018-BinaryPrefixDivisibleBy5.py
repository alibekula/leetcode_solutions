# Last updated: 24.11.2025, 19:49:36
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = int(''.join(map(str, nums)), 2)
        ans = []
        n = len(nums)

        for i in range(n-1, -1, -1):

            ans.append(curr % 5 == 0)

            curr = curr >> 1
        
        ans.reverse()
        return ans
