# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Iteration -- BFS Row-Wise
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return
        res = []
        queue = [root]
        while queue:
            values = []
            for i in queue:
                if i:
                    values.append(i.val)
            print(values, len(values))
            if len(values) > 0:
                res.append(sum(values) * 1. / len(values))
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return res

    # iteration -- BFS Pair-Wise
    def averageOfLevels_1(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            node, dep = queue.pop(0)
            if not node:
                continue
            if dep >= len(res):
                res.append([node.val])
            else:
                res[dep].append(node.val)
            queue.append((node.left, dep + 1))
            queue.append((node.right, dep + 1))
        return [sum(values) * 1. / len(values) for values in res]

    # recursive way
    def averageOfLevels_2(self, root):

        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)

        return [s / float(c) for s, c in info]

