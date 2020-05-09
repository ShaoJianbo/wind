# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        """使用集合存储链表节点"""
        cur = head
        node_dict = {}
        while cur:
            node_dict[cur.val] = cur
            pre, cur = cur, cur.next
            pre.next = None

        head = ListNode(1)
        cur = head
        for key, node in node_dict.items():
            cur.next = node
            cur = cur.next

        return head.next


if __name__ == '__main__':
    so = Solution()
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(1)
    n6 = ListNode(3)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    res = so.removeDuplicateNodes(n1)
    while res:
        print(res.val)
        res = res.next
