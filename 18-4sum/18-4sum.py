# Last updated: 13.08.2025, 17:01:17
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early termination if the smallest possible sum is greater than target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Continue to next iteration if the largest possible sum is smaller than target
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate elements for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Early termination
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                # Continue to next iteration
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        # Skip duplicates for the third number
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        # Skip duplicates for the fourth number
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1

        return res
