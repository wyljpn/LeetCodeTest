# 221. 最大正方形
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4

class Solution(object):
    # 方法一：暴力法
    # 由于正方形的面积等于边长的平方，因此要找到最大正方形的面积，首先需要找到最大正方形的边长，然后计算最大边长的平方即可。
    #
    # 暴力法是最简单直观的做法，具体做法如下：
    #
    # ·遍历矩阵中的每个元素，每次遇到1，则将该元素作为正方形的左上角；
    #
    # ·确定正方形的左上角后，根据左上角所在的行和列计算可能的最大正方形的边长（正方形的范围不能超出矩阵的行数和列数），在该边长范围内寻找只包含1的最大正方形；
    #
    # ·每次在下方新增一行以及在右方新增一列，判断新增的行和列是否满足所有元素都是1。
    def maximalSquare(self, matrix):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                # 遇到一个 1 作为正方形的左上角
                if matrix[i][j] == "1":
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, cols - j)
                    # 判断新增的一行一列是否均为 1
                    for k in range(1, currentMaxSide):
                        flag = True
                        # 判断右下角的位置是否为0
                        if matrix[i + k][j + k] == "0":
                            break
                        # 判断新增的一行一列是否均为1（除了右下角）
                        for m in range(k):
                            if matrix[i + k][j + m] == "0" or matrix[i + m][j + k] == "0":
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break
        maxSquare = maxSide * maxSide
        return maxSquare

    # 方法二：动态规划
    #
    # 可以使用动态规划降低时间复杂度。我们用dp(i, j)表示以(i, j)为右下角，且只包含1的正方形的边长最大值。
    # 如果我们能计算出所有dp(i, j)的值，那么其中的最大值即为矩阵中只包含1的正方形的边长最大值，其平方即为最大正方形的面积。
    #
    # 那么如何计算 dpdp 中的每个元素值呢？对于每个位置 (i, j)(i,j)，检查在矩阵中该位置的值：
    # ·如果该位置的值是 0，则 dp(i, j) = 0，因为当前位置不可能在由 1 组成的正方形中；
    # ·如果该位置的值是 1，则 dp(i, j)的值由其上方、左方和左上方的三个相邻位置的 dp 值决定。具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 1，状态转移方程如下：
    #   dp(i, j) = min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1)) + 1

    def maximalSquare_1(self, matrix):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare



so = Solution()

print(so.maximalSquare([]))
