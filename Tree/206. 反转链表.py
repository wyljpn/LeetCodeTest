# 206. 反转链表
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 方法一：迭代
    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp

        return prev

    # 方法二：递归
    def reverseList_2(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return p

