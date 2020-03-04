# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 两个都不为None
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
        # 一个为None时返回False，或者都为None时返回True
            return p == q

    # DFS with stack
    def isSameTree_2(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            # 两个都为None
            if not node1 and not node2:
                continue
            # 一个为None, 一个不为None
            elif None in [node1, node2]:
                return False
            # 2个都不为None
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True

    # BFS with queue
    def isSameTree_3(self, p, q):
        queue = [(p, q)]
        while queue:
            # pop 出最先进入的queue的tuple
            node1, node2 = queue.pop(0)
            # 两个都为None
            if not node1 and not node2:
                continue
            # 一个为None, 一个不为None
            elif None in [node1, node2]:
                return False
            # 2个都不为None
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True
