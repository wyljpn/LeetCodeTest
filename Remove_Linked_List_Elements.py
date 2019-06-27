# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 创建一个新的Node来当head，这样while的条件就可以直接写p.next了
        head, head.next = ListNode(0), head
        # 创建一个指针来遍历ListNode
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head.next

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node2.next = node3
head.next = node2

so = Solution()
res = so.removeElements(head, 3)
print(res.val)
print(res.next.val)
print(res.next.next)