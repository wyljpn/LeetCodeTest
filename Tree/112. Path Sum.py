# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # DFS
    def hasPathSum(self, root, sum):
        stack = [(root, 0)]

        while stack:
            node, pre_sum = stack.pop()
            if node:
                if not node.left and not node.right and sum == (pre_sum + node.val):
                    return True
                else:
                    stack.append([node.left, pre_sum + node.val])
                    stack.append([node.right, pre_sum + node.val])
        return False

    # recursive
    def hasPathSum_1(self, root, sum):
        def check(node, pre_sum):
            if node and not node.left and not node.right:
                return (pre_sum + node.val) == sum
            elif node:
                return check(node.left, pre_sum + node.val) or check(node.right, pre_sum + node.val)
        if not root:
            return False
        return check(root, 0)


    def hasPathSum_2(self, root, sum):

        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum_2(root.left, sum) or self.hasPathSum_2(root.right, sum)

