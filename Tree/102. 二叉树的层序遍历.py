# 102. 二叉树的层序遍历
#
# 给你一个二叉树，请你返回其按
# 层序遍历
# 得到的节点值。 （即逐层地，从左到右访问所有节点）。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []

        from collections import defaultdict
        from collections import deque

        queue = deque()
        queue.append((root, 0))
        dic = defaultdict(list)

        while queue:
            print(dic)
            node, depth = queue.popleft()
            dic[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return [dic[i] for i in range(len(dic))]