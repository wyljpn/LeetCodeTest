# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # DFS
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            node1, node2 = queue.pop(0)
            # 两个都为None
            if not node1 and not node2:
                continue
            # 其中一个为None
            if None in (node1, node2):
                return False
            # 两个都不为None
            # 两个val相等
            if node1.val == node2.val:
                # 因为是判断镜像，所以要一个分支的left和另一个分支的right进行对比
                queue.append((node1.left, node2.right))
                queue.append((node1.right, node2.left))
            else:
                return False
        return True

    # recursive solution
    def isSymmetric_2(self, root):
        if not root:
            return True

    def isSymmetricTree(self, node1, node2):
        # 两个都不为None
        if node1 and node2:
            return node1.val == node2.val and self.isSymmetric(node1.left, node2.right) and self.isSymmetric(self.right, self.left)
        # 有一个是None时返回False，两个都是None时返回True
        else:
            return node1 == node2
