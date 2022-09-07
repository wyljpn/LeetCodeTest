# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        def traversal(inorder, postorder):
            if not inorder:
                return None

            nodeval = postorder[-1]
            node = TreeNode(nodeval)

            index = inorder.index(nodeval)

            inorder_left = inorder[:index]
            inorder_right = inorder[index + 1:]

            postorder_left = postorder[:len(inorder_left)]
            postorder_right = postorder[len(inorder_left):-1]

            node.left = traversal(inorder_left, postorder_left)
            node.right = traversal(inorder_right, postorder_right)

            return node

        result = traversal(inorder, postorder)

        return result