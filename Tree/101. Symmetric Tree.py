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

    # recursive solutions
    def isSymmetric_2(self, root):
        def isSym(L, R):

            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)

            return L == R
        return not root or isSym(root, root)

    # BFS
    # 一次检查一层
    def isSymmetric_3(self, root):
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]: return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True