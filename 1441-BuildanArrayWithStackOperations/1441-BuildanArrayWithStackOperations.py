# Last updated: 22.11.2025, 23:36:41
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        p = 0
        ans = []

        for i in range(1, n + 1):
            if i == target[p]:
                p += 1
                ans.append('Push')

                if p == len(target):
                    break
            else:
                ans.append('Push')
                ans.append('Pop')
        
        return ans
