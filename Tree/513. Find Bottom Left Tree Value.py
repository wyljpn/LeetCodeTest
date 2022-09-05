# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root):
        from collections import deque

        que = deque()

        que.append(root)

        result = 0

        while que:
            size = len(que)

            result = que[0].val

            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return result

    def findBottomLeftValue_2(self, root):

        max_depth = float('-inf')
        leftmost_val = 0

        def traversal(node, curDepth):
            nonlocal max_depth, leftmost_val
            if (not node.left) and (not node.right):
                if curDepth > max_depth:
                    max_depth = curDepth
                    leftmost_val = node.val

            if node.left:
                curDepth += 1
                traversal(node.left, curDepth)
                curDepth -= 1

            if node.right:
                curDepth += 1
                traversal(node.right, curDepth)
                curDepth -= 1

        if not root:
            return 0

        traversal(root, 0)

        return leftmost_val
