# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        stack = [(root, float('inf'), 0)]
        while stack:
            node, parent_val, length = stack.pop()
            if node.val == parent_val:
                ans = max(ans, length + 1)
            else:
                length = 0
            if node.left:
                stack.append((node.left, node.val, length))
            if node.right:
                stack.append((node.right, node.val, length))
        return ans

    # recursive
    def longestUnivaluePath_1(self, root):
        longest = [0]

        def traverse(node):
            if not node:
                return 0

            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            # 返回上一级
            return max(left, right)

        traverse(root)
        return longest[0]

    # recursive
    def longestUnivaluePath_2(self, root):
        self.longest = 0

        def traverse(node, parent_val):
            if not node:
                return 0
            left, right = traverse(node.left, node.val), traverse(node.right, node.val)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if node.val == parent_val else 0

        traverse(root, None)
        return self.longest
