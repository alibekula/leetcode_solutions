# Last updated: 13.08.2025, 16:59:25
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left_to_right = [1]*len(ratings)
        right_to_left = [1]*len(ratings) 
        ans = [0]*len(ratings)
        
        l, r = 0, len(ratings)-1

        while l + 1 < len(ratings):

            if ratings[l+1] > ratings[l]:
                left_to_right[l+1] = left_to_right[l] + 1

            l += 1

        while r - 1 >= 0:

            if ratings[r-1] > ratings[r]:
                right_to_left[r-1] = right_to_left[r] + 1

            r -= 1
        
        for i in range(len(ans)):
            ans[i] = max(left_to_right[i], right_to_left[i])
        
        return sum(ans)
