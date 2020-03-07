class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast != slow:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
        if not fast or not head.next:
            return None
        else:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow


if __name__ == '__main__':
    so = Solution()
    head = ListNode(1)
    one = ListNode(2)
    two = ListNode(0)
    three = ListNode(-4)
    head.next = one
    one.next = two
    two.next = three
    three.next = one
    res = so.detectCycle(head)
    print(res.val)

    [
        -21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9,
        20, 14, 14, 2, 13, -24, 21, 23, -21, 5
    ]
    24
