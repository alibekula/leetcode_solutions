# Last updated: 18.12.2025, 16:46:22
1# The rand7() API is already defined for you.
2# def rand7():
3# @return a random integer in the range 1 to 7
4
5class Solution:
6    def rand10(self):
7        """
8        :rtype: int
9        """
10        # 1 2 3 4 5 6 7
11        # 8 9 10 11 12 13 14
12        # 7 * (rand7 - 1) + rand7()
13        #  1 2 3 4 5 6 7
14        #1 1 2 3 4 5 6 7
15        #2 8 9 10 11 12 13 14
16        #3 
17        #4
18        #5
19        #6
20        #7
21
22        val = 7 * (rand7() - 1) + rand7()
23
24        if val > 40:
25            return self.rand10()
26        else:
27            return 1 + val % 10