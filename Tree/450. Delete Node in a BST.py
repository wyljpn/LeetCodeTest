# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key):

        def deleteOneNode(target):
            if not target:
                return None

            if not target.right:
                return target.left

            cur = target.right

            while cur.left:
                cur = cur.left

            cur.left = target.left
            target = target.right

            return target

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

        # 要删除的node是root的情况
        if not pre:
            return deleteOneNode(cur)

        # 因为我们需要知道要删除的节点的parent，所以需要pre变量。
        if pre.left and pre.left.val == key:
            pre.left = deleteOneNode(cur)

        if pre.right and pre.right.val == key:
            pre.right = deleteOneNode(cur)

        return root

