# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = head
        pre = None

        while cur: # 因为要链接最后一个item的next到倒数第二个，所以是while cur，而不是cur.next
            cur.next, cur, pre = pre, cur.next, cur

        return pre # 此时cur已经是None，pre是最后一个item


    def reverseList_2(self, head):
        cur = head
        pre = None

        def reverse(cur, pre):
            if not cur:
                return pre

            temp = cur.next
            cur.next = pre
            return reverse(temp, cur)

        return reverse(cur, pre)
