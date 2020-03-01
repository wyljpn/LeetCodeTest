import numpy as np


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        res = 0
        for r in range(M - 2):
            for c in range(N - 2):
                curgrid = [[grid[r + i][c + j] for j in range(3)] for i in range(3)]
                if self.isMagic(curgrid):
                    res += 1

    def isMagic(self, grid):
        count = range(9)
        for i in range(3):
            for j in range(3):
                if not (1 <= grid[i][j] <= 9):
                    return False
                count[grid[i][j] - 1] += 1
        if 0 in count:
            return False
        row, col = [0, 0, 0], [0, 0, 0]
        for i in range(3):
            row[i] += sum(grid[i][j] for j in range(3))
        if row[0] != row[1] != row[2]:
            return False

        for j in range(3):
            col[j] = sum(grid[i][j] for i in range(3))
        if col[0] != col[1] != col[2]:
            return False

        if grid[0][0] + grid[2][2] != grid[0][2] + grid[2][0]:
            return False
        return True


so = Solution()
print(so.numMagicSquaresInside([
    [4, 3, 8, 4],
    [9, 5, 1, 9],
    [2, 7, 6, 2]]))

print(so.numMagicSquaresInside(
    [[1, 1, 1],
     [4, 5, 6],
     [9, 9, 9]]))

print(so.numMagicSquaresInside(
    [[4, 7, 8],
     [9, 5, 1],
     [2, 3, 6]]))
