class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r_index, c_index = 0, 0
        for i in range(len(board)):
            if "R" in board[i]:
                r_index = i
                c_index = board[i].index("R")
                break
        # print(r_index)
        # print(c_index)

        cnt = 0
        for i in range(r_index - 1, -1, -1):
            # print(board[i][c_index])
            if board[i][c_index] == "B":
                break
            if board[i][c_index] == "p":
                cnt += 1
                break
        for i in range(r_index + 1, len(board)):
            if board[i][c_index] == "B":
                break
            if board[i][c_index] == "p":
                cnt += 1
                break

        for j in range(c_index - 1, -1, -1):
            if board[r_index][j] == "B":
                break
            if board[r_index][j] == "p":
                cnt += 1
                break

        for j in range(c_index + 1, len(board[0])):
            if board[r_index][j] == "B":
                break
            if board[r_index][j] == "p":
                cnt += 1
                break

        return cnt


    def numRookCaptures_1(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j
        res = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + i, y0 + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p': res += 1
                if board[x][y] != '.': break
                x, y = x + i, y + j
        return res


so = Solution()

print(so.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                          [".", ".", ".", "p", ".", ".", ".", "."],
                          [".", ".", ".", "R", ".", ".", ".", "p"],
                          [".", ".", ".", ".", ".", ".", ".", "."],
                          [".", ".", ".", ".", ".", ".", ".", "."],
                          [".", ".", ".", "p", ".", ".", ".", "."],
                          [".", ".", ".", ".", ".", ".", ".", "."],
                          [".", ".", ".", ".", ".", ".", ".", "."]]))

print(so.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                          [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                          [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))

print(so.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                          [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                          [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
