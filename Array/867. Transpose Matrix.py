class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        res = []
        for i in range(n):
            new_row = []
            for j in range(m):
                new_row.append(A[j][i])
            res.append(new_row)
        return res

    def transpose_1(self, A):
        # https://leetcode.com/problems/transpose-matrix/discuss/146797/C%2B%2BJavaPython-Easy-Understood
        # https://stackoverflow.com/questions/5239856/asterisk-in-function-call
        # * operator, [ [ 1, 2 ], [ 3, 4 ] ] -> [ 1, 2 ], [ 3, 4 ], then zip takes [1,3], [2,4], ...
        return list(zip(*A))


so = Solution()

print(so.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(so.transpose([[1,2,3],[4,5,6]]))
