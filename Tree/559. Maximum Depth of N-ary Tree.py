"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):

    # DFS
    def maxDepth(self, root):

        def dfs(root):
            if not root:
                return 0
            res = 0
            for child in root.children:
                res = max(dfs(child), res)
            return res + 1

        return dfs(root)


    # BFS
    def maxDepth_1(self, root):
        if not root:
            return 0
        if not root.children:
            return 1

        max_depth= 0
        q=[root, None]
        while len(q) > 0:
            node = q.pop(0)
            if node == None:
                max_depth +=1
                if len(q):
                    q.append(None)
                continue
            if node and node.children:
                for c in node.children:
                    q.append(c)
        return max_depth

    # BFS
    def maxDepth_2(self, root):
        q, level = root and [root], 0
        while q:
            q, level = [child for node in q for child in node.children if child], level + 1
        return level
