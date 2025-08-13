# Last updated: 13.08.2025, 16:56:56
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def is_uniform(self, row, col, n, grid):
        first = grid[row][col]

        for i in range(row, row+n):
            for j in range(col, col+n):
                if grid[i][j] != first:
                    return  False, 1
        return True, first

    def build_tree(self, i, j, size, grid):

        uniform, val = self.is_uniform(i, j, size, grid)

        if uniform:
            return Node(val, 1, None, None, None, None) 
        else:
            new_size = size//2

            topleft = self.build_tree(i, j, new_size, grid)
            topright = self.build_tree(i, j+new_size, new_size, grid)
            bottomleft = self.build_tree(i+new_size, j, new_size, grid)
            bottomright = self.build_tree(i+new_size, j+new_size, new_size, grid)

            return Node(val, 0, topleft, topright, bottomleft, bottomright)

    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.build_tree(0, 0, len(grid), grid)