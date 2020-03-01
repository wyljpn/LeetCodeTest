import numpy as np
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        np_A = np.array(A)
        # print(np_A)

        for i in range(len(A)):
            # print("test", np_A[i, :] == 0)
            np_A[i,:] = np_A[i][::-1]

            np_A[i, np_A[i,:] == 0 ] = 2
        np_A -= 1
        # print(np_A)
        return np_A.tolist()

    def flipAndInvertImage_1(self, A):
        return [ [1 ^ i for i in reversed(row)] for row in A]


so = Solution()
print(so.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(so.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))