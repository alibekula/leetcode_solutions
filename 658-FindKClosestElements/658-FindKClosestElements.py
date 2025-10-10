# Last updated: 10.10.2025, 22:36:07
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        l, r = 0, n-k-1

        # 1 2 3 4 5 6 k = 3, x = 3
        while l <= r:
            mid = (l+r)//2

            if x - arr[mid] <= arr[mid+k] - x:
                r = mid - 1
            else:
                l = mid + 1

        return arr[l: l+k] 