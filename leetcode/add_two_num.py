# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        res = l3 = ListNode(0)
        next_val = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + next_val
            # print("sum_val", sum_val)
            if sum_val >= 10:
                sum_val -= 10
                next_val = 1
            else:
                next_val = 0
            l3.next = ListNode(sum_val)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            pass
        elif l2:
            l1 = l2

        while l1:
            print("l1-->", l1.val, "next_val", next_val)
            sum_val = l1.val + next_val
            if sum_val >= 10:
                sum_val -= 10
                next_val = 1
            else:
                next_val = 0
            l3.next = ListNode(sum_val)
            l3 = l3.next
            l1 = l1.next

        if next_val > 0:
            l3.next = ListNode(next_val)
            l3 = l3.next
        return res.next


if __name__ == '__main__':
    l1 = ListNode(9)
    l12 = ListNode(8)
    l13 = ListNode(3)
    l1.next = l12
    # l12.next = l13

    l21 = ListNode(1)
    l22 = ListNode(6)
    l23 = ListNode(4)

    # l21.next = l22
    # l22.next = l23

    so = Solution()
    res = so.addTwoNumbers(l1, l21)
    while res:
        print("res-->", res.val)
        res = res.next
