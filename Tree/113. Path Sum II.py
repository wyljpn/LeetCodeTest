# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # DFS + stack II
    def pathSum(self, root, target):
        stack = [(root, [])]
        res = []

        while stack:
            node, pre_list = stack.pop()
            if node:
                if not node.left and not node.right and target == (sum(pre_list) + node.val):
                    pre_list.append(node.val)
                    res.append(pre_list)
                if node.left:
                    stack.append([node.left, pre_list + [node.val]])
                if node.right:
                    stack.append([node.right, pre_list + [node.val]])
        return res

    def pathSum_1(self, root, target):
        def dfs(root, target, ls, res):
            if not root.left and not root.right and target == root.val:
                ls.append(root.val)
                res.append(ls)
            if root.left:
                dfs(root.left, target - root.val, ls + [root.val], res)
            if root.right:
                dfs(root.right, target - root.val, ls + [root.val], res)

        if not root:
            return []
        res = []
        dfs(root, target, [], res)

    def pathSum_2(self, root, target):
        if not root:
            return []
        # 只有当叶子的val等于target的时候才返回值
        if not root.left and not root.right and target == root.val:
            return [[root.val]]
        tmp = self.pathSum_2(root.left, target - root.val) + self.pathSum_2(root.right, target - root.val)
        # 返回node的val和其子节点的val
        return [[root.val] + i for i in tmp]

    # BFS + queue
    def pathSum_3(self, root, target):
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == target:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))
        return res

    # DFS + stack I
    def pathSum_4(self, root, target):
        if not root:
            return []
        res = []
        stack = [(root, target - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
        return res

