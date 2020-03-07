# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return []

        stack = [(root, root.val)]
        while stack:
            node, right_sum = stack.pop()

            if node.right:
                stack.append((node.right, right_sum+node.val))
            if node:
                node.val = right_sum
            if node.left:
                stack.append((node.left, right_sum+node.val))

        return root

    # recursive
    def convertBST_1(self, root):
        self.right_part_sum = 0

        def visit(node):
            if node:
                visit(node.right)
                node.val += self.right_part_sum
                self.right_part_sum = node.val
                visit(node.left)
        visit(root)
        return root


    sum_values = 0
    def convertBST_2(self, root):
        if not root:
            return None
        self.convertBST_2(root.right)
        self.sum_values += root.val
        root.val = self.sum_values
        self.convertBST_2(root.left)
        return root
