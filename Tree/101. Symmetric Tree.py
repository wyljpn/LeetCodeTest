# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # DFS
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            node1, node2 = queue.pop(0)
            # 两个都为None
            if not node1 and not node2:
                continue
            # 其中一个为None
            if None in (node1, node2):
                return False
            # 两个都不为None
            # 两个val相等
            if node1.val == node2.val:
                # 因为是判断镜像，所以要一个分支的left和另一个分支的right进行对比
                queue.append((node1.left, node2.right))
                queue.append((node1.right, node2.left))
            else:
                return False
        return True

    # recursive solutions
    def isSymmetric_2(self, root):
        if not root:
            return True

        def compare(left, right):
            # 首先排除空节点的情况
            if left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left == None and right == None:
                return True
            # 排除了空节点，再排除数值不相同的情况
            elif left.val != right.val:
                return False

            # 此时就是：左右节点都不为空，且数值相同的情况
            # 此时才做递归，做下一层的判断
            outside = compare(left.left, right.right)  # 左子树：左、 右子树：右
            inside = compare(left.right, right.left)  # 左子树：右、 右子树：左
            isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
            return isSame

        return compare(root.left, root.right)

    # BFS
    # 一次检查一层
    def isSymmetric_3(self, root):

        if not root:
            return True
        import collections
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        while queue: #接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左节点为空、右节点为空，此时说明是对称的
                continue

            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True