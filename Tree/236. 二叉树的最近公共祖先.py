# 236. 二叉树的最近公共祖先
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):


    # 递归，
    # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    # 方法二：存储父节点
    def lowestCommonAncestor_2(self, root, p, q):
        parent = {}
        visited = set()
        def dfs(root):
            if not root.left:
                parent[root.left.val] = root
                dfs(root.left)
            if not root.right:
                parent[root.right.val] = root
                dfs(root.right)

        dfs(root)

        while not p:
            visited.add(p.val)
            p = parent.get(p.val)

        while not q:
            if q.val in visited:
                return q
            q = parent.get(q.val)
        return