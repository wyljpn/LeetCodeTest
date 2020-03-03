# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

    def addTwoNumbers_1(self, l1, l2):
        def toInt(node):
            return node.val + 10 * toInt(node.next) if node else 0

        def toList(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = toList(n / 10)
            return node

        return toList(toInt(l1) + toInt(l2))

    