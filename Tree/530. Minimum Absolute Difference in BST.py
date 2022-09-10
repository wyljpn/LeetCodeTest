# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        L = []

        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)

        dfs(root)
        # 因为是binary search tree， 所以中序遍历得到的L是升序的。
        # 如果用其他顺序的话，需要在加上abs
        return min(b - a for a, b in zip(L, L[1:]))


    def getMinimumDifference_1(self, root):

        self.ans = float('inf')
        self.prev = None

        def search(node):
            if node.left:
                search(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            if node.right:
                search(node.right)
        search(root)
        return self.ans

    def getMinimumDifference_2(self, root):

        stack = []
        cur = root
        prev_node = None
        min_diff = float("INF")

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                if prev_node:
                    min_diff = min(min_diff, cur.val - prev_node.val)

                prev_node = cur
                cur = cur.right

        return min_diff