# coding=utf-8

# 210. 课程表 II
# 现在你总共有 n 门课需要选，记为 0 到 n-1。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
#
# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: [0,1]
# 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。


class Solution(object):


    # 方法一：入度表（广度优先遍历）
    def findOrder(self, numCourses, prerequisites):
        from collections import deque

        res = []

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
            res.append(pre)
            numCourses -= 1
            # 将此节点对应所有邻接节点 cur 的入度 -1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                # 如果入度变为0，则说明其前驱节点都被删除。此时将其添加入队列。
                if not indegrees[cur]:
                    queue.append(cur)
        # 如果所有节点都被删除，则代表能修完所有课程。
        return res if not numCourses else []


    # 方法二：深度优先遍历
    def findOrder_2(self, numCourses, prerequisites):

        res = []
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]

        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            # 遍历i课程的前驱课程
            for j in adjacency[i]:
                # 如果后续课程已被当前节点启动的 DFS 访问。就是说存在环。
                if not dfs(j, adjacency, flags):
                    return False

            # 将此课程设置为已经被满足
            flags[i] = -1
            res.append(i)
            return True

        # 添加以cur的前驱
        for cur, pre in prerequisites:
            adjacency[cur].append(pre)

        # 判断每个节点起步的DFS是否存在环
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return []
        return res