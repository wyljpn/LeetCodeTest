# coding:utf-8
# 面试题04. 二维数组中的查找
#
# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
#  
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        row_idx, col_idx = 0, cols -1
        while row_idx < rows and col_idx >= 0:
            # print("row_idx:", row_idx)
            # print("col_idx:", col_idx)
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] > target:
                col_idx -= 1
            elif matrix[row_idx][col_idx] < target:
                row_idx += 1
        return False


so = Solution()

print(so.findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))
print(so.findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 20))
print(so.findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 18))