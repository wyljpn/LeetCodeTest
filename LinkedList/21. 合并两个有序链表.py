# 21. 合并两个有序链表
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 迭代
    def mergeTwoLists(self, l1, l2):

        # head is used to keep the first node
        # prev is used to make the previous node
        prev = head = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # Link to the rest part of list1 or list2
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2

        return head.next

    # 递归
    def mergeTwoLists_1(self, l1, l2):
        # 如果其中一个list为空，则结果的尾部接上另一个list的部分。
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 如果当前list1的node小于list2的，list1的下一个node与list2的剩余部分比较
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists_1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_1(l1, l2.next)
            return l2




def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next



def printList(l: ListNode):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


so = Solution()

l1 = generateList([1])
l2 = generateList([1, 3, 4])

printList(so.mergeTwoLists(l1, l2))