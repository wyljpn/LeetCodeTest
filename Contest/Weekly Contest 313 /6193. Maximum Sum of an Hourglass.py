# You are given an m x n integer matrix grid.
#
# We define an hourglass as a part of the matrix with the following form:
#

# Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
# Output: 30
# Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.

# Constraints:
#
# m == grid.length
# n == grid[i].length
# 3 <= m, n <= 150
# 0 <= grid[i][j] <= 106

class Solution:
    def maxSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        result = 0

        for i in range(n-2):
            for j in range(1, m-1):
                sum = grid[i][j-1] + grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+2][j-1] + grid[i+2][j] + grid[i+2][j+1]
                result = max(sum, result)

        return result

if __name__ == "__main__":
    so = Solution()

    print(so.maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))
    print(so.maxSum([[1,2,3],[4,5,6],[7,8,9]]))