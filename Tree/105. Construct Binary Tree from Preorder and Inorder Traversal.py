class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        def traversal(preorder, inorder):
            if not preorder:
                return None

            nodeval = preorder[0]
            node = TreeNode(nodeval)

            index = inorder.index(nodeval)

            inorder_left = inorder[:index]
            inorder_right = inorder[index + 1:]

            preorder_left = preorder[1:len(inorder_left) + 1]
            preorder_right = preorder[len(inorder_left) + 1:]

            node.left = traversal(preorder_left, inorder_left)
            node.right = traversal(preorder_right, inorder_right)

            return node

        result = traversal(preorder, inorder)

        return result