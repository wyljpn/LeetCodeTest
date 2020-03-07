# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # DFS
    def binaryTreePaths(self, root):
        res = []
        stack = [(root, [])]
        while stack:
            node, lst = stack.pop()
            if not node.left and not node.right:
                res.append('->'.join(lst + [str(node.val)]))
            if node.right:
                stack.append((node.right, lst + [str(node.val)]))
            if node.left:
                stack.append((node.left, lst + [str(node.val)]))
        return res

    # BFS
    def binaryTreePaths_1(self, root):
        if not root:
            return []
        res = []
        queue = [(root, "")]
        while queue:
            node, ls = queue.pop(0)
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + '->'))
            if node.right:
                queue.append((node.right, ls + str(node.val) + '->'))
        return res

    # recursive
    def binaryTreePaths_2(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.binaryTreePaths_2(root.left)] + \
               [str(root.val) + '->' + i for i in self.binaryTreePaths_2(root.right)]

