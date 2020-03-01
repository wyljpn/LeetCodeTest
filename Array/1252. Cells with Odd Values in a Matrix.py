import numpy as np
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        mat = np.zeros([n, m])

        for ri, ci in indices:
            mat[ri,:] = (mat[ri, :] + 1) % 2
            mat[:, ci] = (mat[:, ci] + 1) % 2

        return int(np.sum(mat))



    def oddCells_1(self, n, m, indices):
        odd_count = 0
        rows = [0]*n
        cows = [0]*m

        for i, j in indices:
            rows[i] = rows[i] ^ 1
            cows[j] = cows[j] ^ 1

        for i in range(n):
            for j in range(m):
                if rows[i] ^ cows[j] == 1:
                    odd_count+=1
        return odd_count

so = Solution()

print(so.oddCells(2, 3, [[0,1],[1,1]]))
print(so.oddCells(2, 2, [[1,1],[0,0]]))