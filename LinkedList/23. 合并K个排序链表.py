# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # 分治法，两两合并链表
    def mergeKLists(self, lists):
        amount = len(lists)

        interval = 1

        # 通过while
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        # 声明头节点和构建链表的节点
        head = point = ListNode(0)

        # 将两个链表头节点进行比较
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next

        if l1:
            point.next = l1
        if l2:
            point.next = l2

        return head.next


    # 使用优先队列。小顶堆。  ps： 没有特别设置大顶堆的方法，如果想要使用大顶堆，则将值加一个负号再加入小顶堆中，使用的时候再加负号。
    def mergeKLists_2(self, lists):
        if not lists or len(lists) == 0:
            return None

        import heapq
        heap = []

        # 首先for嵌套while就是将所有元素都取出放入堆
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node =node.next
        dummy = ListNode(None)
        cur = dummy

        # 依次将堆种的元素取出（因为是小顶堆，所以每次出来的都是目前堆种最小的元素），然后重新构建一链表返回。
        while heap:
            temp_node = ListNode(heapq.heappop(heap))
            cur.next = temp_node
            cur = cur.next
        return dummy.next

