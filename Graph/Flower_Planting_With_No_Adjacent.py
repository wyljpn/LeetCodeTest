class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # 下标从0开始
        res = [0] * N
        # 标记相邻的garden
        G = [[] for i in range(N)]
        for x, y in paths:
            # 因为题目中garden的编号是从1开始，
            # 但是res从0开始，需要统一下标。
            # 这边将garden的下标要-1。
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
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

so = Solution()
print(so.gardenNoAdj(3, [[1,2],[2,3],[3,1]]))