# 98. 验证二叉搜索树
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true

# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 方法一: 递归
    # 思路和算法
    #
    # 要解决这道题首先我们要了解二叉搜索树有什么性质可以给我们利用，由题目给出的信息我们可以知道：如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值； 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；它的左右子树也为二叉搜索树。

    def isValidBST(self, root):

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >=upper:
                return False

            # 右子树。值要大于node.val，并且小于upper
            if not helper(node.right, val, upper):
                return False

            # 左子树。值要小于node.val
            if not helper(node.left, lower, val):
                return False

            return True

        return helper(root)

    # 方法二：中序遍历
    # 基于方法一中提及的性质，我们可以进一步知道二叉搜索树「中序遍历」得到的值构成的序列一定是升序的，
    # 这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
    # 如果均大于说明这个序列是升序的，整棵树是二叉搜索树，否则不是，下面的代码我们使用栈来模拟中序遍历的过程。

    def isValidBST_2(self, root):
        stack, inorder = [], float('-inf')

        while stack or root:
            # 将当前节点和其左节点都添加到stack中
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val

            # 如果是left节点，因为其right为None，所以下一轮将pop出其root。
            # 如果是root节点，下一轮pop出right
            # 如果是right节点并且其rigth为空，则下一轮pop出其root的root。
            # 如果是right节点并且其rigth不为空，则下一轮将添加其right的左节点。
            root=root.right

        return True
