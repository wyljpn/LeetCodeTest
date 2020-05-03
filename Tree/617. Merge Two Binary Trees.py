# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # recursive
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

    # Iterative
    # 合并到t1上
    def mergeTrees_1(self, t1, t2):
        if t1 is None:
            return t2

        stack = []
        stack.append((t1, t2))
        while stack:
            n1, n2 = stack.pop()
            if not n2:
                continue
            n1.val += n2.val
            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))
            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))
        return t1

    # Iterative
    # 新建一个Tree
    def mergeTrees_2(self, t1, t2):
        dummy = TreeNode(0)
        stack = [(t1, t2, dummy, 'l')]
        while stack:
            n1, n2, present, lr = stack.pop()
            n = TreeNode((n1.val if n1 else 0) + (n2.val if n2 else 0)) if n1 or n2 else None
            if lr == 'l':
                present.left = n
            else:
                present.right = n

            if n1 or n2:
                # In the statement A and B, Python Compiler will check A first, if A is False it returns A without checking B. But if A is True, it continues to check B and returns whatever value of B.
                stack.append((n1 and n1.left, n2 and n2.left, n, 'l'))
                stack.append((n1 and n1.right, n2 and n2.right, n, 'r'))

        return dummy.left