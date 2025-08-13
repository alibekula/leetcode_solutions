# Last updated: 13.08.2025, 17:01:27
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x <= 9:
            return True
        
        arr = []
        curr = x

        while curr:
            tmp = curr%10
            curr = curr//10
            arr.append(tmp)
        
        l, r = 0, len(arr)-1

        while l <= r:
            if arr[l] != arr[r]:
                return False

            l += 1
            r -= 1

        return True 
        