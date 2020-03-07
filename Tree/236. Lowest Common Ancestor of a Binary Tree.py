# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        stack = [(root, [])]
        p_list = []
        q_list = []
        while stack:
            node, lst = stack.pop()
            if node:
                print(lst)
                # if p_list and q_list:
                # break
                if node.val == p.val:
                    print("==p", node.val, lst)
                    p_list = lst
                if node.val == q.val:
                    print("==q", node.val, lst)
                    q_list = lst
                if node.right:
                    stack.append((node.right, lst + [node.val]))
                if node.left:
                    stack.append((node.left, lst + [node.val]))
        for i, j in zip(p_list, q_list):
            if i == j:
                return i

        return None

    def lowestCommonAncestor_1(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor_2(self, root, p, q):
        answer = []
        stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                parent += node if all(subs) else max(subs)
        return answer[0]

    def lowestCommonAncestor_3(self, root, p, q):
        def path(root, goal):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == goal:
                            return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()

        return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)
