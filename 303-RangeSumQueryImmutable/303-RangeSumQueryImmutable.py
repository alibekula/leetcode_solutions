# Last updated: 13.08.2025, 16:57:55
class NumArray:

    def __init__(self, nums: List[int]):
        self.left_to_right = [0]
        n = len(nums)
        for i in range(n):
            self.left_to_right.append(self.left_to_right[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.left_to_right[right+1] - self.left_to_right[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)