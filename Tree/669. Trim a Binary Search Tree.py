# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        
        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

    def trimBST_2(self, root, low, high):
        if not root:
            return None

        # 把root移动到[low, high]中
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left

        # 把root的左子树中小于low的部分移除
        # 一直往左下角遍历，当遇到小于low的node，就检查那个node的右子树
        cur = root
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left

        # 把root的右子树中大于high的部分移除
        cur = root
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right

        return root