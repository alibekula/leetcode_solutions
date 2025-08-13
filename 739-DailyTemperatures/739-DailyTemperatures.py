# Last updated: 13.08.2025, 16:57:00
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)
        
        return res