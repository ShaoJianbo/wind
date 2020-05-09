# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = tail
            tail = cur
            cur = next_node
        return tail

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            p_head = l1
            p_head.next = self.mergeTwoLists(l1.next, l2)
        else:
            p_head = l2
            p_head.next = self.mergeTwoLists(l1, l2.next)
        return p_head




if __name__ == "__main__":
    so = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    res = so.reverseList(n1)
    while res:
        print(f"{res.val}-->")
        res = res.next
