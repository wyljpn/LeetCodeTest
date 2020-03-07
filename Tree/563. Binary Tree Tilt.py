# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def tilt(node):
            if not node:
                return 0
            left = tilt(node.left)
            right = tilt(node.right)
            print(node.val, left, right, abs(left - right))
            self.res += abs(left - right)
            return node.val + left + right

        tilt(root)
        return self.res