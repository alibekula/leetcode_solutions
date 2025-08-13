# Last updated: 13.08.2025, 16:56:18
class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        if not nums:
            return False

        if len(nums)%2 != 0:
            return False

        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0

            counter[num] += 1

        for key, value in counter.items():
            if counter[key] % 2 != 0:
                return False
        
        return True
            


        