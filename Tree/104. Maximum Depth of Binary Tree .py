# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # BFS + deque
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            curr, val = queue.pop(0)
            # 因为是BFS,最后一次的循环一定是深度最深的node。返回此node的val即是最大深度。
            if not curr.left and not curr.right and not queue:
                return val
            if curr.left:
                queue.append((curr.left, val + 1))
            if curr.right:
                queue.append((curr.right, val + 1))

    # DFS
    def maxDepth_2(self, root):
        res = 0
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            # 计算到叶子时，取叶子的深度与全局深度的较大值
            if not node:
                res = max(res, level)
            else:
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return res

    # recursive solution
    def maxDepth_3(self, root):
        if not root:
            return 0
        # 从叶子往root计算，叶子为1，每个父节点取子节点中的较大值。
        return max(self.maxDepth_3(root.left), self.maxDepth_3(root.right)) + 1
