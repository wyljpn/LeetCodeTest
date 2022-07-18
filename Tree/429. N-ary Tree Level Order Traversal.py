"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        from collections import deque
        from collections import defaultdict

        que = deque()
        que.append((root, 0))

        nodes_at_depth = defaultdict(list)

        while que:
            node, depth = que.popleft()
            nodes_at_depth[depth].append(node.val)

            if node.children:
                for subtree in node.children:
                    que.append((subtree, depth+1))

        return [nodes_at_depth[depth] for depth in range(len(nodes_at_depth))]