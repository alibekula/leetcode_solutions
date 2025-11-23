# Last updated: 23.11.2025, 20:59:25
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dct = {0:[], 1:[], 2:[]}
        for num in nums:
            dct[num % 3].append(num)

        total = sum(nums)
        if total % 3 == 0:
            return total

        dct[1].sort()
        dct[2].sort()

        INF = 10**18
        rem = total % 3

        remove_one_from_1 = dct[1][0] if len(dct[1]) >= 1 else INF
        remove_two_from_2 = (dct[2][0] + dct[2][1]) if len(dct[2]) >= 2 else INF

        remove_one_from_2 = dct[2][0] if len(dct[2]) >= 1 else INF
        remove_two_from_1 = (dct[1][0] + dct[1][1]) if len(dct[1]) >= 2 else INF

        if rem == 1:
            min_remove = min(remove_one_from_1, remove_two_from_2)
        else:  # rem == 2
            min_remove = min(remove_one_from_2, remove_two_from_1)

        if min_remove >= INF:
            return 0
        return total - min_remove
