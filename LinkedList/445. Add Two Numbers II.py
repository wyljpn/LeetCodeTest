# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 使用栈后，再使用头插法即可
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        head = ListNode(0)
        carry = 0

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2:
            res = 0
            if stack1:
                res += stack1.pop()
            if stack2:
                res += stack2.pop()
            carry, res = divmod(res + carry, 10)

            p = ListNode(res)
            p.next = head.next
            head.next = p
        if carry != 0:
            p = ListNode(carry)
            p.next = head.next
            head.next = p

        return head.next


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
    l1 = generateList([7,2,4,3])
    l2 = generateList([3,5, 6, 4])
    # printList(l1)
    # printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
