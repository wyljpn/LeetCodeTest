# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        startx, starty = 0, 0
        loop = min(m // 2, n // 2)

        res = [0] * (m * n)
        counter = 0

        for offset in range(1, loop + 1):
            for j in range(starty, n - offset):
                res[counter] = matrix[startx][j]
                counter += 1

            for i in range(startx, m - offset):
                res[counter] = matrix[i][n-offset]
                counter += 1

            for j in range(n - offset, starty, -1):
                res[counter] = matrix[m-offset][j]
                counter += 1

            for i in range(m - offset, startx, -1):
                res[counter] = matrix[i][starty]
                counter += 1
            startx += 1
            starty += 1

        if counter < (m*n):
            if (n -m) >= 1:
                res[counter:] = matrix[loop][starty:n-starty]
            elif (m - n) >= 1:
                for i in range(starty, m-startx):
                    res[counter] = matrix[i][startx]
                    counter += 1
            else:
                res[counter] = matrix[loop][loop]

        return res

if __name__ == "__main__":
    so = Solution()
    print(so.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(so.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(so.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]))
    print(so.spiralOrder([[2,5],[8,4],[0,-1]]))
