# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    # Has error, when [1], 1
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return []

        fast, slow = head, head

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


    def removeNthFromEnd_2(self, head, n):
        if not head:
            return []

        # Added a dummy head to fix the issue
        dummy_head = ListNode(next=head)

        fast, slow = dummy_head, dummy_head

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_head.next