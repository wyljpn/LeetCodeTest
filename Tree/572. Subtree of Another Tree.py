# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # 每个s的node与t的root比较，如果相同的话，就接着比较
    def isSubtree(self, s, t):

        def isIdentical(p, q):
            if p and q:
                return p.val == q.val and isIdentical(p.left, q.left) and isIdentical(p.right, q.right)
            else:
                return p == q

        if isIdentical(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # [3,4,5,1,2]  ^3#^4#^1#$$^2#$$^5#$$
    # [4,1,2]         ^4#^1#$$^2#$$
    # DFS， 先序
    # ^ 跟 node.val
    # # 跟 node.left
    # $ 当 node 为None
    def isSubtree_1(self, s, t):
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        print(t)
        print(s)
        return convert(t) in convert(s)