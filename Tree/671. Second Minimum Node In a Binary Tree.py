# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):

        if not root:
            return -1
        min_val = root.val
        second_min_val = float('inf')

        stack = [root]
        while stack:
            node = stack.pop()
            if second_min_val > node.val > min_val:
                second_min_val = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return -1 if second_min_val == float('inf') else second_min_val

    # recursive
    def findSecondMinimumValue_1(self, root):

        res = [float('inf')]

        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)

        return -1 if res[0] == float('inf') else res[0]
