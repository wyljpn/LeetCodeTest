# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def traversal(root):
            if root == None:
                return

            traversal(root.left)
            traversal(root.right)
            res.append(root.val)

        traversal(root)

        return res

    def postorderTraversal_2(self, root):

        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            result.append(node.val)
            if node.right:
                result.append(node.right)
            if node.left:
                result.append(node.left)

        return result[::-1]


        return result
