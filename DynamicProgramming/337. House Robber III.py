# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        left, right = self.traversal(root)
        return max(left, right)

    def traversal(self, node):
        if not node:
            return (0, 0)

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        return (max(left[0], left[1]) + max(right[0], right[1]), node.val + left[0] + right[0])