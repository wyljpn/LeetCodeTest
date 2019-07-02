class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * N
        # 标记相邻的garden
        G = [[] for i in range(N)]
        for x, y in paths:
            #  因为编号是从1开始，所以下标要-1。
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            # 减去第i个garden所连接的garden的花的type。然后选从中选一个。
            # i=0: {1,2,3,4} - {与0号garden相邻的花的type}  pop:4
            # i=1: {1,2,3,4} - {与1号garden相邻的花的type}  pop:
            # i=2: {1,2,3,4} - {与2号garden相邻的花的type}  pop:
            # i=3: {1,2,3,4} - {与3号garden相邻的花的type}  pop:
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res

    # dfs, directed graph painting
    def gardenNoAdj_2(self, N, paths):
        res = [None] * (N + 1)
        # space optimization, use directed graph, neighbor_index < cur_index
        paths = map(sorted, paths)
        import collections
        graph = collections.defaultdict(list)
        for neighbor, cur in paths:
            graph[cur].append(neighbor)
        import random
        # dfs painting, check colors used by connected neighbor nodes
        def dfs(cur):
            used_colors = set(res[neighbor] for neighbor in graph[cur])
            while True:
                color = random.randint(1, 4)
                if color not in used_colors:
                    res[cur] = color
                    break

        # space optimization, call dfs() from low to high node index
        for cur in range(1, N + 1):
            dfs(cur)

        return res[1:]
