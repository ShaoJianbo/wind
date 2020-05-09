# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """删除链表"""
        if not head:
            return head
        pre = head
        cur = pre
        while cur.val != val:
            pre = cur
            cur = cur.next

        if head is cur:
            new_head = head.next
            head.next = None
            del head
            return new_head
        else:
            pre.next = cur.next
            cur.next = None
            del cur
            return head


if __name__ == '__main__':
    so = Solution()
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    res = so.deleteNode(n1, 5)

    while res:
        print(res.val)
        res = res.next
