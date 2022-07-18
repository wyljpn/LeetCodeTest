# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        from collections import deque
        from collections import defaultdict

        que = deque()
        que.append((root, 0))

        max_value_at_layer = defaultdict(lambda: float("-inf"))

        while que:
            node, depth = que.popleft()
            max_value_at_layer[depth] = max(node.val, max_value_at_layer[depth])

            if node.left:
                que.append((node.left, depth + 1))

            if node.right:
                que.append((node.right, depth + 1))

        return [max_value_at_layer[depth] for depth in range(len(max_value_at_layer))]