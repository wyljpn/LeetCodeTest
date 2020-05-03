# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#
# 示例 1:
# 输入:
#
# 0 0 0
# 0 1 0
# 0 0 0
# 输出:
#
# 0 0 0
# 0 1 0
# 0 0 0

class Solution(object):
    def updateMatrix(self, matrix):
        import  collections
        M, N = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = [[0] * N for _ in range(M)]
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if matrix[x][y] == 1:
                    res[x][y] = step
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= M or newy < 0 or newy >= N or visited[newx][newy] == 1:
                        continue
                    queue.append((newx, newy))
                    visited[newx][newy] = 1
            step += 1
        return res
