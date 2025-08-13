# Last updated: 13.08.2025, 17:00:28
class Solution:
    from collections import deque
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        ans = []
        add = 0

        while pointer >= 0:
            if pointer == len(digits) - 1:
                tmp = digits[pointer] + 1
            else:
                tmp = digits[pointer]

            tmp += add
            add = tmp // 10
            tmp %= 10

            ans.append(tmp)
            pointer -= 1

        if add:
            ans = ans + [add]

        return ans[::-1]