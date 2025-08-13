# Last updated: 13.08.2025, 16:59:05
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1 

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
