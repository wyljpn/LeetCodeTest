# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dic = {}

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if dic.get(node.val, float('-inf')) != float('-inf'):
                    return True
                else:
                    dic[k - node.val] = node.val
                print(node.val, k - node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def findTarget_1(self, root, k):
        s = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    
