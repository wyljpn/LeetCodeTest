# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode

        根据快慢法则，走得快的一定会追上走得慢的。
        在这道题中，有的链表短。它走完之后去走另一条链表，我们可以理解成快的指针。

        两个指针会在第二次经过交接点时汇合。因为交接点之后的长度一样，走的交接点之前的距离也一样。
        """

        if headA is None or headB is None:
            return None

        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next if curA.next else headB
            curB = curB.next if curB.next else headA

        return curA



    def getIntersectionNode2(self, headA, headB):

        if headA is None or headB is None:
            return None

        curA, curB = headA, headB
        lenA, lenB = 0, 0

        while curA:
            lenA += 1
            curA = curA.next

        while curB:
            lenB += 1
            curB = curB.next

        if lenB > lenA:
            curA, curB = headB, headA
            lenA, lenB = lenB, lenA
        else:
            curA, curB = headA, headB

        gap = lenA - lenB
        while gap > 0:
            curA = curA.next
            gap -= 1

        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA