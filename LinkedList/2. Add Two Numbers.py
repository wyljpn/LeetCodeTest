# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # wyl
    def addTwoNumbers(self, l1, l2):

        res = ListNode(None)
        tmp = res

        carry = 0
        while l1 or l2 or carry != 0:
            if l1 and l2:
                carry, val = divmod(l1.val + l2.val + carry, 10)
                l1, l2 = l1.next, l2.next
            elif l1 and not l2:
                carry, val = divmod(l1.val + carry, 10)
                l1 = l1.next
            elif not l1 and l2:
                carry, val = divmod(l2.val + carry, 10)
                l2 = l2.next
            elif carry == 1:
                carry, val = 0, 1
            else:
                break
            node = ListNode(val)
            tmp.next = node
            tmp = tmp.next
        return res.next


    def addTwoNumbers(self, l1, l2):
        prenode = ListNode(0)
        lastnode = prenode
        carry = 0
        while carry or l1 or l2:
            carry, cur = divmod(carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next


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


if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
