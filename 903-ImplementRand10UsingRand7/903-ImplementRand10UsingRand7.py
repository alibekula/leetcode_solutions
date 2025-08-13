# Last updated: 13.08.2025, 16:56:50
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number from 1 to 49
            x = (rand7() - 1) * 7 + rand7()
            # Only accept if it's in the range 1 to 40
            if x <= 40:
                # Use modulo to get a result in the range 1 to 10
                return x % 10 + 1
