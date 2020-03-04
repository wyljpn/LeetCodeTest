# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isBalanced_1(self, root):

        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        if not root:
            return True

        return abs(getHeight(root.left) - getHeight(root.right)) < 2 and self.isBalanced_1(root.left) and self.isBalanced_1(
            root.right)

    # recursive
    def isBalanced_2(self, root):

        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or (left-right) > 1:
                return -1
            return 1 + max(left, right)

        return  check(root) != -1
