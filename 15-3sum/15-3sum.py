# Last updated: 13.08.2025, 17:01:21
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort to handle duplicates easily
        num_to_index = {}  # Store last index of each number
        res = set()  # Store unique triplets
        
        # Step 2: Populate dictionary
        for i, num in enumerate(nums):
            num_to_index[num] = i  # Store last occurrence
        
        # Step 3: Iterate with two nested loops (but skipping duplicates)
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate `i` values
                continue
                
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate `j` values
                    continue

                key = -(nums[i] + nums[j])  # Find third number

                # Step 4: Check if third number exists and isn't reusing `i` or `j`
                if key in num_to_index and num_to_index[key] > j:
                    res.add((nums[i], nums[j], key))  # Store as tuple to avoid duplicates

        return list(map(list, res))  # Convert set to list of lists
