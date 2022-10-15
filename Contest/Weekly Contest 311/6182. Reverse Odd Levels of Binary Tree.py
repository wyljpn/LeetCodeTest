#
# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
# * For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root):

        from collections import deque
        que = deque([root])
        dep = 1

        next_level_val = []

        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()

                if cur.left:
                    que.append(cur.left)
                    if dep % 2 == 1:
                        next_level_val.append(cur.left.val)
                if cur.right:
                    que.append(cur.right)
                    if dep % 2 == 1:
                        next_level_val.append(cur.right.val)

                if dep % 2 == 0:
                    if len(next_level_val) > 0:
                        cur.val = next_level_val.pop()

            if dep % 2 == 0:
                next_level_val = []
            dep += 1

        return root