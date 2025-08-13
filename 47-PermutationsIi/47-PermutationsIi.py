# Last updated: 13.08.2025, 17:00:47
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        dct = {}
        lst = []

        for num in nums:
            if num not in dct:
                dct[num] = 0
            dct[num] += 1
        
        def backtrack(curr):
            if len(curr) == len(nums):
                lst.append(curr[:])
                return 
            
            for val in dct:
                if dct[val] > 0:
                    dct[val] -= 1
                    curr.append(val)

                    backtrack(curr)

                    val = curr.pop()
                    dct[val] += 1
                    
            
        backtrack([])
        return lst
                    




