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

    # Traversal way
    def searchBST_2(self, root, val):

        def traversal(node, val):
            if not node or node.val == val:
                return node

            if node.left and node.val > val:
                return traversal(node.left, val)

            if node.right and node.val < val:
                return traversal(node.right, val)

            return None

        return traversal(root, val)


    # 迭代法。因为只要查找其中一条path，不用遍历所有path，所以可以替换root来查找。
    def searchBST_3(self, root, val):

        # 当root变成None当时候，退出循环，并且返回None
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root

        return None