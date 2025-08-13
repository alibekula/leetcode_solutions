# Last updated: 13.08.2025, 16:56:13
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        def find_l():
            l, r = 0, len(nums)-1
            pos_l = None

            while l <= r:
                mid = (l+r)//2

                if nums[mid] == 0:
                    pos_l = mid
                    r = mid - 1
                elif nums[mid] > 0:
                    r = mid - 1
                
                elif nums[mid] < 0:
                    l = mid + 1
            
            return pos_l if pos_l else l
        
        def find_r():
            l, r = 0, len(nums)-1
            pos_r = None

            while l <= r:
                mid = (l+r)//2

                if nums[mid] == 0:
                    pos_r = mid
                    l = mid + 1
                elif nums[mid] > 0:
                    r = mid - 1
                
                elif nums[mid] < 0:
                    l = mid + 1
            
            return pos_r if pos_r else r

        return max(find_l() , len(nums)-find_r()-1)

        