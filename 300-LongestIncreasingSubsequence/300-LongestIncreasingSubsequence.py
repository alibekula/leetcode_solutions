# Last updated: 13.08.2025, 16:57:56
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def bin_search(array, target):
            l, r = 0, len(array)-1

            while l <= r:
                mid = (l+r)//2

                if array[mid] == target:
                    return mid
                
                if array[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return l
        
        ans = []

        for num in nums:
            if not ans or ans[-1] < num:
                ans.append(num)
            else:
                idx = bin_search(ans, num)
                ans[idx] = num
        
        return len(ans)
                

