# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        dic = {}

        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                dic[node.val] = dic.get(node.val, 0) + 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        max_cnt = max(dic.values())
        res = []
        for key, val in dic.items():
            if val == max_cnt:
                res.append(key)
        return res

    def findMode_1(self, root):
        if not root:
            return []
        import collections
        count = collections.Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.values())
        return [k for k, v in count.items() if v == max_ct]

    def helper(self, root, cache):
        if root == None:
            return
        cache[root.val] += 1
        self.helper(root.left, cache)
        self.helper(root.right, cache)
        return

    def findMode_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import defaultdict
        if root == None:
            return []
        cache = defaultdict(int)
        self.helper(root, cache)
        max_freq = max(cache.values())
        result = [k for k, v in cache.items() if v == max_freq]
        return result
