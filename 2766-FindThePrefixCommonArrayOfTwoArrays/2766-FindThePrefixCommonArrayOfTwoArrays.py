# Last updated: 13.08.2025, 16:56:09
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = [0]*(len(A)+1)
        ans = []
        curr = 0

        for i in range(len(A)):

            common[A[i]] += 1

            if common[A[i]] >= 2:
                curr += 1
            
            common[B[i]] += 1

            if common[B[i]] >= 2:
                curr += 1
            
            ans.append(curr)
        
        return ans