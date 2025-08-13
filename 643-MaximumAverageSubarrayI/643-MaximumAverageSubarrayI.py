# Last updated: 13.08.2025, 16:57:08
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = 0
        n = len(nums)

        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum / k

        for j in range(k, n):
            curr_sum += nums[j]
            curr_sum -= nums[j-k]
            avg = curr_sum/k
            max_avg = max(max_avg, avg)

        return max_avg
                    