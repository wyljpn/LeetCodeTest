class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        if len(moves) < 5:
            return "Pending"

        win_pattern = [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8], [0,4,8], [2,4,6]]

        A = []
        B = []
        for i in range(len(moves)):
            if i % 2 == 0:
                A.append(moves[i][0] * 3 + moves[i][1])
            else:
                B.append(moves[i][0] * 3 + moves[i][1])

        for patter in win_pattern:
            if len(set(A).intersection(set(patter)))==3:
                return "A"
            if len(set(B).intersection(set(patter)))==3:
                return "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

    def tictactoe_1(self, moves):
        row, col = [[0]*3 for _ in range(2)], [[0]*3 for _ in range(2)]
        d1, d2, id = [0] *2, [0]*2, 0
        for r,c in moves:
            row[id][r] += 1
            col[id][c] += 1
            d1[id] += r == c
            d2[id] += r+c ==2
            if 3 in (row[id][r], col[id][c], d1[id], d2[id]):
                return "AB"[id]
            id ^= 1
        return 'Draw' if len(moves) == 9 else "Pending"

so = Solution()

print(so.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(so.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(so.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(so.tictactoe([[0,0],[1,1]]))