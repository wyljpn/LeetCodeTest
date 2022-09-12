# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key):

        def deleteOneNode(node):
            if not node:
                return None

            if not node.right:
                return node.left

            cur = node.right

            while cur.left:
                cur = cur.left

            cur.left = node.left
            node = node.right

            return node

        if not root:
            return []

        cur = root
        pre = None

        while cur:
            if cur.val == key:
                break

            pre = cur

            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right

        if pre == None:
            return deleteOneNode(cur)

        if pre.left and pre.left.val == key:
            pre.left = deleteOneNode(cur)

        if pre.right and pre.right.val == key:
            pre.right = deleteOneNode(cur)

        return root