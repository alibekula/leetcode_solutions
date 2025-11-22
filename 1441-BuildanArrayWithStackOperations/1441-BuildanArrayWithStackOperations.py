# Last updated: 22.11.2025, 23:35:04
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        inside = 0
        stack = []
        dct = {str(key): 0 for key in range(n)}

        for log in logs:
            idx0, op, ts = log.split(':')
            ts = int(ts)

            if op == 'end':

                idx1, start = stack.pop()
                dct[idx0] += ts - start + 1

                if stack:
                    idx2 = stack[-1][0]
                    dct[idx2] -= ts-start +1 
            else:
                stack.append([idx0, ts])
        
        return list(dct.values())


