# Last updated: 10.10.2025, 22:57:33
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        prefix = {}
        n = len(A)
        count = 0
        ans = []
        
        for i in range(1, n+1):
            prefix[i] = [False, False]
        

        for i in range(n):
            
            val1 = A[i]
            prefix[val1][0] = True

            if prefix[val1][1] == True:
                count += 1
            
            val2 = B[i]
            prefix[val2][1] = True

            if prefix[val2][0] == True:
                count += 1
            
            ans.append(count)
        
        return ans
