# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # dfs recursively
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node, level, res):
        if node:
            # 新的level
            if len(res) < level + 1:
                res.insert(0, [])
            # 添加val到当前层的List. 倒数是从-1开始，所以要+1
            res[-(level + 1)].append(node.val)
            self.dfs(node.left, level + 1, res)
            self.dfs(node.right, level + 1, res)

    # dfs + stack
    def levelOrderBottom_2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                # 应该level是从0而不是1开始的，所以跟len比较的时候要加1
                if len(res) < level + 1:
                    res.insert(0, [])
                # 颠倒顺序
                res[-(level + 1)].append(node.val)
                # 因为要求是从左到右，所以right,left,栈顶取left
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res

    # bfs + queue
    def levelOrderBottom_3(self, root):
        import collections
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append([node.left, level + 1])
                queue.append([node.right, level + 1])
        return res
