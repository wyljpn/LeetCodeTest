# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):

        def traversal(nums):
            if not nums:
                return None

            maxvalue = max(nums)
            index = nums.index(maxvalue)
            node = TreeNode(maxvalue)

            node.left = traversal(nums[:index])
            node.right = traversal(nums[index + 1:])

            return node

        if not nums:
            return None

        result = traversal(nums)

        return result