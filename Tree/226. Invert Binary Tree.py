# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    # DFS
    def invertTree_1(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                # 添加入stack的顺序不重要，因为node其实在上一句已经交换过了
                stack.extend([node.right, node.left])
        return root

    # BFS
    def invertTree_2(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                # 添加入queue的顺序不重要，因为node其实在上一句已经交换过了
                queue.append(node.left)
                queue.append(node.right)
        return root