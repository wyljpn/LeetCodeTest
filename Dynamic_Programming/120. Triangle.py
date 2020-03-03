class Solution(object):
    # # O(n*n/2) space, top-down
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = [[0 for i in range(len(row))] for row in triangle]

        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j], res[i - 1][j - 1]) + triangle[i][j]
        return min(res[-1])

    # Modify the original triangle, top-down
    def minimumTotal_1(self, triangle):
        if not triangle:
            return
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j ==0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) -1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

    # Bottom-up, O(n) space
    def minimumTotal_2(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1])+triangle[i][j]
        return res[0]


    # Modify the original triangle, bottom-up
    def minimumTotal_3(self, triangle):
        if not triangle:
            return
        for i in range(len(triangle) -2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1])
        return triangle[0][0]




