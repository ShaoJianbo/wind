
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        """反转列表"""

        if not head:
            return []
        tail = ListNode("my")
        tail = None
        cur_node = head
        next_node = head.next

        cur_node.next = tail
        tail = cur_node

        while next_node:
            cur_node = next_node
            next_node = next_node.next
            cur_node.next = tail
            tail = cur_node

        ans = []
        while cur_node:
            ans.append(cur_node.val)
            cur_node = cur_node.next

        return ans


if __name__ == '__main__':
    so = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    res = so.reversePrint(n1)
    print(res)
