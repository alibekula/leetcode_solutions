# Last updated: 10.10.2025, 17:01:24
from collections import deque
class Solution:
    def maximumSwap(self, num: int) -> int:

        if num < 10:
            return num
        
        nums = list(str(num))
        n = len(nums)
        dct = {}

        for i in range(n):
            digit = int(nums[i])
            if digit not in dct:
                dct[digit] = deque()
            
            dct[digit].append(i)
        
        for i in range(n):
            dig = int(nums[i])
            dct[dig].popleft()

            if not dct[dig]:
                del dct[dig]

            if dig == 9:
                continue
            
            seq = []
            for j in range(dig+1, 10):
                if j in dct and dct[j]:
                    idx = dct[j].pop()
                    seq.append([j, idx])

            if seq:
                idx = max(seq, key=lambda x: x[0])[1]
                nums[idx], nums[i] = nums[i], nums[idx]
                return int(''.join(nums))
            
        return num



