#
#
# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
# Example 2:
# Input: n = 1
# Output: [[1]]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        startx, starty = 0, 0
        offset = 0
        loop = n // 2
        counter = 1
        res = [[0 for i in range(n)] for i in range(n)]
        print("res: ", res)

        # 牢记左闭右开的原则
        for l in range(loop):
            print("l: ", l)
            for j in range(starty, n - 1 - offset):
                print("left->right")
                print("j: ", j)
                print("starty: ", starty)
                res[startx][j] = counter
                print("res: ", res)
                counter += 1
            for i in range(startx, n - 1 - offset):
                print("top->buttom")
                print("i: ", i)
                print("startx: ", startx)
                res[i][n-1-starty] = counter
                print("res: ", res)
                counter += 1
            for j in range(n - 1 - starty, offset, -1):
                print("right->left")
                print("j: ", j)
                print("starty: ", starty)
                res[n-1-starty][j] = counter
                print("res: ", res)
                counter += 1
            for i in range(n - 1 - startx, offset, -1):
                print("bottom->top")
                print("i: ", i)
                print("starty: ", starty)
                res[i][starty] = counter
                print("res: ", res)
                counter += 1

            startx += 1
            starty += 1
            offset += 1

        if n % 2 == 1:
            res[n//2][n//2] = counter

        return res

if __name__ == "__main__":
    so = Solution()
    print(so.generateMatrix(2))
    # print(so.generateMatrix(3))
    # print(so.generateMatrix(4))
    # print(so.generateMatrix(5))