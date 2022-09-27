# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original, clonedcloned, target):

        stack = [clonedcloned]

        while stack:
            node = stack.pop()

            if node.val == target.val:
                return node

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return None

    def getTargetCopy_2(self, original, cloned, target):

        def traversal(node, target):
            if not node:
                return None

            if node.val == target.val:
                return node

            return traversal(node.left, target) or traversal(node.right, target)

        return traversal(cloned, target)