# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root, val):

        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == val:
                return node
            elif node.val > val:
                if not node.left:
                    return None
                else:
                    stack.append(node.left)
            elif node.val < val:
                if not node.right:
                    return None
                else:
                    stack.append(node.right)

        return None