class Solution(object):
    def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True


    def isToeplitzMatrix_1(self, m):
        return all(m[i][j] == m[i+1][j+1] for i in range(len(m-1)) for j in range(len(m[0])-1))

    def isToeplitzMatrix_2(self, m):
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(m, m[1:]))


so = Solution()
# print(so.isToeplitzMatrix([
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]))
#
# print(so.isToeplitzMatrix([
#   [1,2],
#   [2,2]
# ]))

# print(so.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

# print(so.isToeplitzMatrix([[65,98,57]]))
print(so.isToeplitzMatrix([[11,74,7,93],[40,11,74,7]]))
