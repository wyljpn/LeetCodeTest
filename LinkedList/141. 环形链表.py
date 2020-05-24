# 141. 环形链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # hash table
    def hasCycle(self, head):
        nodesSeen = set()
        while head:
            if head in nodesSeen:
                return True
            else:
                nodesSeen.add(head)
            head = head.next
        return False

    # 快慢指针
    # 通过使用具有 不同速度 的快、慢两个指针遍历链表，空间复杂度可以被降低至 O(1)。慢指针每次移动一步，而快指针每次移动两步。
    def hasCycle_2(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True