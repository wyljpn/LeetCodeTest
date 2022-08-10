# void backtracking(参数) {
#     if (终止条件) {
#         存放结果;
#         return;
#     }
#
#     for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
#         处理节点;
#         backtracking(路径，选择列表); // 递归
#         回溯，撤销处理结果
#     }
# }

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def backTracking(n, k, startIndex):
            if len(path) == k:
                result.append(path[:])  # 复制值，生成新的list
                return

            for i in range(startIndex, n + 1):  # 遍历当前层
                path.append(i)     # 处理当前值
                backTracking(n, k, i + 1)   # 递归
                path.pop()         # 回溯

        backTracking(n, k, 1)
        return result