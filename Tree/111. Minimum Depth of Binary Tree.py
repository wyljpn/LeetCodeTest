# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # bFS
    def minDepth(self, root):
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if node:
                # 应为是按层遍历，第一次出现没有leaf的node就是最短的路径
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))

    # DFS + recursive
    def minDepth_1(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth_1(root.left), self.minDepth_1(root.right)) + 1
        else:
            return max(self.minDepth_1(root.left), self.minDepth_1(root.right)) + 1

    # DFS
    def minDepth_2(self, root):
        if not root:
            return 0

        stack = [(root, 1)]
        res = float('inf')

        while stack:
            node, depth = stack.pop()
            if node:
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
            if node and not node.left and not node.right:
                res = min(res, depth)

        return res
