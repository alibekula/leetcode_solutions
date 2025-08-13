# Last updated: 13.08.2025, 17:00:42
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        if len(nums) == 1:
            return nums[0]
        curr_num = 0
        for num in nums:
            curr_num = max(curr_num + num, num)
            max_sum = max(curr_num, max_sum)
        return max_sum

            



        