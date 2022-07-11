# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def traversal(root):
            if root == None:
                return

            traversal(root.left)
            res.append(root.val)
            traversal(root.right)

        traversal(root)

        return res