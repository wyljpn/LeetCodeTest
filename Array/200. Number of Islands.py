class Solution(object):

    # 从一个岛的起点开始，将其连接的点都设置为0
    def dfs(self, grid, r, c):
        # 将其设置为0
        grid[r][c] = "0"
        nr, nc = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            newr, newc = r + dr, c + dc
            if 0 <= newr < nr and 0 <= newc < nc and grid[newr][newc] == "1":
                self.dfs(grid, newr, newc)

    # dfs
    def numIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands

    # bfs
    def numIslands_1(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    import collections
                    neighbors = collections.deque([(r, c)])
                    # 从一个岛的起点开始，将其连接的点都设置为0。
                    while neighbors:
                        row, col = neighbors.popleft()
                        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                        for dr, dc in dirs:
                            newr, newc = row + dr, col + dc
                            if 0 <= newr < nr and 0 <= newc < nc and grid[newr][newc] == "1":
                                neighbors.append((newr, newc))
                                grid[newr][newc] = "0"
        return num_islands

    # union find
    def numIslands_2(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            # 合并两个相邻为1的节点
                            uf.union(r * nc + c, x * nc + y)
        return uf.getCount()


class UnionFind:

    # 初始化，将所有为"1"的节点都设置为root
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    # 查找节点对应的根节点
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # 使两棵树并成一棵树
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    # 返回树的数量
    def getCount(self):
        return self.count


so = Solution()

print(so.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(so.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))

print(so.numIslands_1(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(so.numIslands_1(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
