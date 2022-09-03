"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):

        if not root:
            return None

        from collections import deque

        que = deque()
        que.append(root)

        while que:
            layer, size = [], len(que)

            for i in range(size):
                node = que.popleft()
                layer.append(node)

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            for i in range(len(layer) - 1):
                layer[i].next = layer[i + 1]

        return root
