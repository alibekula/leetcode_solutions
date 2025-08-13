# Last updated: 13.08.2025, 16:56:37
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        if not firstList or not secondList:
            return []

        ans = []
        l, r = 0, 0

        while r < len(secondList) and l < len(firstList):
            left = max(firstList[l][0], secondList[r][0])
            right = min(firstList[l][1], secondList[r][1])

            if left <= right:
                ans.append([left, right])
            
            if firstList[l][1] >= secondList[r][1]:
                if r < len(secondList):
                    r += 1
            else:
                if l < len(firstList):
                    l += 1

        return ans