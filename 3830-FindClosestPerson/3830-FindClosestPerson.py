# Last updated: 06.09.2025, 21:51:02
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first_dist = abs(x-z)
        second_dist = abs(y-z)

        if first_dist < second_dist:
            return 1
        elif first_dist > second_dist:
            return 2
        else:
            return 0