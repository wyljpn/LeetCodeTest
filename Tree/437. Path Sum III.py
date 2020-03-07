# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def find_paths(root, target):
            if root:
                # 以当前节点为终点，或者其left或right为终点进行判断。
                return int(root.val == target) + find_paths(root.left, target - root.val) + find_paths(root.right,
                                                                                                       target - root.val)
            return 0

        if root:
            # pathSum 以root.left或者root.right为新的root进行查找
            return find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


    