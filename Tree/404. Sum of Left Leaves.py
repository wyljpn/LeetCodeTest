# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        res = 0

        # is_left
        stack = [(root, False)]

        while stack:
            node, is_left = stack.pop()
            if not node.left and not node.right and is_left:
                print(node.val)
                res += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))
        return res

    # recursive
    def sumOfLeftLeaves_1(self, root):
        def dfs(root, is_left=False):
            if not root:
                return 0
            if is_left and not root.left and not root.right:
                return root.val
            return dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)

   