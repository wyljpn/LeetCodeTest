# coding=utf-8

# 207. 课程表
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#  
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

class Solution(object):
    # 方法一：入度表（广度优先遍历）
    # 算法流程：
    # 1.统计课程安排图中每个节点的入度，生成 入度表 indegrees。
    # 2.借助一个队列 queue，将所有入度为 00 的节点入队。
    # 3.当 queue 非空时，依次将队首节点出队，在课程安排图中删除此节点 pre：
    #   `并不是真正从邻接表中删除此节点 pre，而是将此节点对应所有邻接节点 cur 的入度 -1，即 indegrees[cur] -= 1。
    #   `当入度 -1−1后邻接节点 cur 的入度为 00，说明 cur 所有的前驱节点已经被 “删除”，此时将 cur 入队。
    # 4.在每次 pre 出队时，执行 numCourses--；
    #   `若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。换个角度说，若课程安排图中存在环，一定有节点的入度始终不为 0。
    #   `因此，拓扑排序出队次数等于课程个数，返回 numCourses == 0 判断课程是否可以成功安排。
    def canFinish(self, numCourses, prerequisites):
        from collections import deque

        # 入度表
        indegrees = [0 for _ in range(numCourses)]
        # 邻接表
        adjacency = [[] for _ in range(numCourses)]

        queue = deque()

        # Get the indegree and adjacency of every course.
        # 统计课程安排图中每个节点的入度.
        # 添加邻接节点
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        # Get all the courses with the indegree of 0.
        # 将所有入度为 0 的节点入队。
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)

        # BFS TopSort.
        while queue:
            # 在课程安排图中删除此节点
            pre = queue.popleft()
            numCourses -= 1
            # 将此节点对应所有邻接节点 cur 的入度 -1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                # 如果入度变为0，则说明其前驱节点都被删除。此时将其添加入队列。
                if not indegrees[cur]:
                    queue.append(cur)
        # 如果所有节点都被删除，则代表能修完所有课程。
        return not numCourses

    # 方法二：深度优先遍历
    # 原理是通过 DFS 判断图中是否有环。
    #
    # 算法流程：
    # 1.借助一个标志列表 flags，用于判断每个节点 i （课程）的状态：
    #   1)未被 DFS 访问：i == 0；
    #   2)已被其他节点启动的 DFS 访问：i == -1；
    #   3)已被当前节点启动的 DFS 访问：i == 1。
    # 2.对 numCourses 个节点依次执行 DFS，判断每个节点起步 DFS 是否存在环，若存在环直接返回 False。DFS 流程；
    #   1)终止条件：
    #      `当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索，直接返回 True。
    #      `当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 22 次访问，即 课程安排图有环 ，直接返回 False。
    #   2)将当前访问节点 i 对应 flag[i] 置 1，即标记其被本轮 DFS 访问过；
    #   3)递归访问当前节点 i 的所有邻接节点 j，当发现环直接返回 False；
    #   4)当前节点所有邻接节点已被遍历，并没有发现环，则将当前节点 flag 置为 -1 并返回 True。
    # 3.若整个图 DFS 结束并未发现环，返回 True。

    def canFinish_2(self, numCourses, prerequisites):

        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            # 遍历i课程的后续课程
            for j in adjacency[i]:
                # 如果后续课程已被当前节点启动的 DFS 访问。就是说存在环。
                if not dfs(j, adjacency, flags):
                    return False
            # 将此课程设置为已经被满足
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]

        # 添加以pre为前驱的课程
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        # 判断每个节点起步的DFS是否存在环
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False

        return True
