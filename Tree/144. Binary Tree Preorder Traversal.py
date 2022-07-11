# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def traversal(root):
            if root == None:
                return

            res.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)

        return res


    def preorderTraversal_2(self, root):
        res = []

        if not root:
            return []

        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
