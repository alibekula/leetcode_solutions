# Last updated: 22.11.2025, 20:42:29
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        l, r = 0, n

        while r < 2 * n:

            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r += 1
        
        return ans

