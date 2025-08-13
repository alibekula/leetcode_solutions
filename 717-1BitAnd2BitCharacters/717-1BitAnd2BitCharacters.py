# Last updated: 13.08.2025, 16:57:01
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0

        while i < n - 1:  # Stop before the last character
            if bits[i] == 1:
                i += 2  # Two-bit character
            else:
                i += 1  # One-bit character

        # If we stopped at the second-to-last index, the last character is one-bit
        return i == n - 1